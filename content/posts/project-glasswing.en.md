---
title: "Project Glasswing: When AI Finds the Bugs Humans Miss"
date: 2026-04-16
lastmod: 2026-06-07
slug: "project-glasswing"
translationKey: "project-glasswing"
description: "Anthropic's Project Glasswing shows that AI can help with defensive security. The hard part for teams becomes triage, patching, rollout, observability and operations."
tags: ["AI", "Cybersecurity", "DevOps", "Platform Engineering", "Open Source"]
categories: ["Technology", "DevOps"]
author: "Evgeny Karpov"
summary: "Project Glasswing is interesting because AI can find more security flaws. But the practical bottleneck becomes everything afterwards: triage, patching, rollout, observability and incident response."
ShowReadingTime: true
---

# Project Glasswing: When AI Finds the Bugs Humans Miss

In April 2026, Anthropic launched **Project Glasswing**: an initiative where frontier AI is used defensively to find and fix security vulnerabilities in critical software.

The most striking example is a **27-year-old vulnerability in OpenBSD**. According to Anthropic's technical write-up, Claude Mythos Preview also showed significantly stronger ability to find, reproduce and in some cases exploit vulnerabilities than previous models.

That is not only interesting for security researchers. It is interesting for everyone who builds and operates software.

## What We Know, And What I Read From It

What is confirmed is that Anthropic presents Project Glasswing as a defensive security initiative, and that its own evaluation of Claude Mythos Preview shows stronger cybersecurity capabilities than earlier models.

My analysis is this:

If tools like this become common, security work becomes less dependent on whether someone finds the bug at all. More bugs will be found. Faster.

That moves the pressure.

From discovery to delivery.

From:

> Can we find the vulnerability?

to:

> Can we react without breaking production?

## What Does This Mean For DevOps?

As a DevOps and infrastructure person, I do not only think:

> AI can find more bugs.

I think:

- How fast can we triage findings?
- How fast can we patch?
- How safely can we deploy?
- Can we see the effect in logs and dashboards?
- Do we have rollback ready if a security fix breaks something?

If AI increases the speed of vulnerability discovery, the bottleneck quickly becomes everything afterwards: prioritization, testing, release, communication and operations.

That is where DevOps matters. Not as a buzzword, but as the practical discipline connecting development, security and production.

## A Practical Defensive List

If you want to prepare for a world with AI-assisted vulnerability discovery, I would start here:

- Know your most important open source dependencies and their owners.
- Create an SBOM or another dependency overview for critical systems.
- Make sure dependency scanning is actually followed up.
- Make patch deployments faster and less dramatic.
- Have good environments for testing security fixes.
- Use observability to see whether fixes change system behavior.
- Document how critical vulnerabilities are prioritized.
- Practice rollback before you face an urgent case on a Friday afternoon.
- Let AI help with analysis, but keep human validation.

## Questions Danish Teams Should Ask

I would start with five practical questions:

1. Who owns our most critical dependencies?
2. How fast can we patch a critical vulnerability in production?
3. Can we see in logs, metrics and traces whether the patch changes system behavior?
4. Who may approve an emergency deployment?
5. Do we have a runbook that actually works under pressure?

If the answer is unclear, AI is not the problem yet. The problem is that the organization has not built the muscle to react.

The positive part is that the tools are now beginning to reach defenders.

It is a race, and we should make sure they win it.

Read also:

- [DevOps Is Not a Pipeline](/karpov-blog/en/posts/devops-is-not-a-pipeline/)
- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)

---

Sources:

- [Anthropic: Project Glasswing](https://www.anthropic.com/project/glasswing)
- [Anthropic Frontier Red Team: Assessing Claude Mythos Preview's cybersecurity capabilities](https://red.anthropic.com/2026/mythos-preview/)
