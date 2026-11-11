<#
Generates the 1200x630 social share images in static/images/og/.

  default.png / default.en.png   site-wide fallback (home, portfolio, about, lists)
  digest.png                     shared by every weekly research digest
  ai-raadgivning.png             the AI-rådgivning page (front matter: ogImage)
  <post-file-name>.png           one per published, non-digest post
  <post-file-name>.en.png        one per published English translation

layouts/partials/og-image.html picks the right file at build time, so a post
without its own image still gets a correct branded card. Run this after adding
or retitling a post, then commit the PNGs:

  pwsh -NoProfile -File scripts/make_og_images.ps1

Windows only (System.Drawing). The build itself does not depend on it.
#>
[CmdletBinding()]
param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$outDir = Join-Path $Root 'static/images/og'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$W = 1200; $H = 630; $Pad = 72

function Get-FontFamily([string[]]$names) {
    $installed = [System.Drawing.FontFamily]::Families.Name
    foreach ($n in $names) { if ($installed -contains $n) { return $n } }
    return 'Arial'
}
$mono = Get-FontFamily @('Cascadia Mono', 'Cascadia Code', 'Consolas')
$sans = Get-FontFamily @('Segoe UI Semibold', 'Segoe UI', 'Arial')

function Get-Color([string]$hex) { [System.Drawing.ColorTranslator]::FromHtml($hex) }

function New-OgImage {
    param(
        [string]$Path,
        [string]$Command,      # text after the prompt, e.g. "cat my-post.md"
        [string]$Title,
        [string]$Footer = 'Evgeny Karpov'
    )

    $bmp = [System.Drawing.Bitmap]::new($W, $H)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    try {
        $g.SmoothingMode = 'AntiAlias'
        $g.TextRenderingHint = 'AntiAliasGridFit'

        $rect = [System.Drawing.Rectangle]::new(0, 0, $W, $H)
        $bg = [System.Drawing.Drawing2D.LinearGradientBrush]::new($rect, (Get-Color '#0b1120'), (Get-Color '#060a16'), 90)
        $g.FillRectangle($bg, $rect)
        $g.FillRectangle([System.Drawing.SolidBrush]::new((Get-Color '#38bdf8')), 0, 0, $W, 8)

        # Prompt line: evgeny@kbh:~$ <command>
        $promptFont = [System.Drawing.Font]::new($mono, 22, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
        $fmt = [System.Drawing.StringFormat]::GenericTypographic
        $fmt.FormatFlags = $fmt.FormatFlags -bor [System.Drawing.StringFormatFlags]::MeasureTrailingSpaces
        $x = [float]$Pad; $y = [float]84
        foreach ($part in @(
                @('evgeny@kbh', '#86efac'), @(':', '#94a3b8'), @('~', '#38bdf8'), @('$ ', '#94a3b8'), @($Command, '#e6edf3'))) {
            $g.DrawString($part[0], $promptFont, [System.Drawing.SolidBrush]::new((Get-Color $part[1])), $x, $y, $fmt)
            $x += $g.MeasureString($part[0], $promptFont, 2000, $fmt).Width
        }

        # Title: largest size that fits the box.
        $boxW = $W - 2 * $Pad; $boxTop = 160; $boxH = 330
        $titleFmt = [System.Drawing.StringFormat]::new()
        $titleFmt.Trimming = 'EllipsisWord'
        $size = 76
        do {
            $titleFont = [System.Drawing.Font]::new($sans, $size, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
            $measured = $g.MeasureString($Title, $titleFont, $boxW, $titleFmt)
            if ($measured.Height -le $boxH) { break }
            $size -= 4
        } while ($size -gt 36)
        # GDI+ pads text by roughly a sixth of an em; pull the box left so the title lines up with the prompt.
        $titleRect = [System.Drawing.RectangleF]::new($Pad - [int]($size / 6), $boxTop, $boxW, $boxH)
        $g.DrawString($Title, $titleFont, [System.Drawing.SolidBrush]::new((Get-Color '#f8fafc')), $titleRect, $titleFmt)

        # Footer: rule, name on the left, domain on the right.
        $g.FillRectangle([System.Drawing.SolidBrush]::new((Get-Color '#26324a')), $Pad, $H - 118, $boxW, 2)
        $footFont = [System.Drawing.Font]::new($mono, 26, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
        $g.DrawString($Footer, $footFont, [System.Drawing.SolidBrush]::new((Get-Color '#94a3b8')), [float]$Pad, [float]($H - 92), $fmt)
        $domain = 'karpov.dk'
        $dw = $g.MeasureString($domain, $footFont, 2000, $fmt).Width
        $g.DrawString($domain, $footFont, [System.Drawing.SolidBrush]::new((Get-Color '#38bdf8')), [float]($W - $Pad - $dw), [float]($H - 92), $fmt)

        $bmp.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
    }
    finally {
        $g.Dispose(); $bmp.Dispose()
    }
}

function Get-FrontMatterValue([string]$text, [string]$key) {
    $m = [regex]::Match($text, "(?m)^$key\s*:\s*(.+?)\s*$")
    if (-not $m.Success) { return $null }
    return $m.Groups[1].Value.Trim().Trim('"').Trim("'")
}

$made = @()

New-OgImage -Path (Join-Path $outDir 'default.png') -Command 'cat noter-fra-koebenhavn.md' `
    -Title 'Fra god idé til stabil drift' -Footer 'Evgeny Karpov · DevOps, .NET og AI-systemer'
New-OgImage -Path (Join-Path $outDir 'default.en.png') -Command 'cat notes-from-copenhagen.md' `
    -Title 'From a good idea to stable production' -Footer 'Evgeny Karpov · DevOps, .NET and AI systems'
New-OgImage -Path (Join-Path $outDir 'digest.png') -Command 'tail -f ugens-ai-forskning.log' `
    -Title 'Ugens AI-forskning' -Footer 'Ugentligt researchoverblik · samlet af AI'
# Standalone pages opt in with "ogImage: images/og/<name>.png" in their front matter.
New-OgImage -Path (Join-Path $outDir 'ai-raadgivning.png') -Command 'cat ai-raadgivning.md' `
    -Title 'AI-rådgivning til mindre virksomheder' -Footer 'Evgeny Karpov · faste priser'
$made += 'default.png', 'default.en.png', 'digest.png', 'ai-raadgivning.png'

Get-ChildItem (Join-Path $Root 'content/posts') -Filter '*.md' -File | Where-Object Name -notlike '_index*' | ForEach-Object {
    $text = Get-Content $_.FullName -Raw -Encoding utf8
    if ((Get-FrontMatterValue $text 'draft') -eq 'true') { return }
    if ((Get-FrontMatterValue $text 'authorship') -eq 'ai-assembled-digest') { return }
    $title = Get-FrontMatterValue $text 'title'
    if (-not $title) { return }

    # "post.md" -> post.png, "post.en.md" -> post.en.png (matches .File.ContentBaseName + language).
    $name = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
    $base = $name -replace '\.en$', ''
    New-OgImage -Path (Join-Path $outDir "$name.png") -Command "cat $base.md" -Title $title
    $made += "$name.png"
}

# Remove images whose post no longer exists or is no longer published.
Get-ChildItem $outDir -Filter '*.png' | Where-Object { $made -notcontains $_.Name } | ForEach-Object {
    Remove-Item $_.FullName
    Write-Host "removed $($_.Name)"
}

Write-Host "Wrote $($made.Count) images to $outDir"
