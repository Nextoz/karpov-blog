---
title: "My Obsidian Vault Got a Small Research Department"
date: 2026-05-26
lastmod: 2026-06-07
slug: "my-obsidian-vault-got-a-small-research-department"
draft: false
translationKey: "obsidian-vault-selvforbedrende-graf"
description: "I built an Obsidian setup with graph memory, a daily research scout and blog drafts. Not as magic, but as a practical AI workbench."
summary: "A look inside my Obsidian vault: graph memory, daily research scout, candidate notes and blog drafts. AI as a workbench, not a magic wand."
tags: ["AI", "Obsidian", "DevOps", "Platform Engineering", "Knowledge Management", "AI Agents"]
categories: ["AI", "DevOps", "Technology"]
author: "Evgeny Karpov"
ShowReadingTime: true
cover:
  image: "/karpov-blog/images/obsidian-vault-knowledge-graph.svg"
  alt: "An Obsidian-like knowledge graph across notes, research, job search and blog work."
  caption: "My vault as a graph. It looks a bit like an afterparty for notes, but there is a real idea behind it."
---

# My Obsidian Vault Got a Small Research Department

![An Obsidian-like knowledge graph across notes, research, job search and blog work.](/karpov-blog/images/obsidian-vault-knowledge-graph.svg)

I have done something that sounds slightly dangerous on paper:

I gave my Obsidian vault a small AI agent.

Not an agent with access to buy stocks, delete production or send emails to former managers at 02:13. That would be a different blog post. Possibly a different life.

This agent has a more practical job:

It helps me keep track of knowledge.

More precisely, I built two things on top of my Obsidian vault:

1. A **self-improving graph memory** that scans my notes and finds holes in the graph.
2. A **daily research scout** that looks for new research and relevant AI/tech news, creates a briefing, creates candidate notes and suggests blog drafts.

That may sound like something from a pitch deck with too many gradients.

The idea is more humble:

I do not want AI to think for me.

I want a workbench that makes it easier to think.

## The Problem With Notes Is Not Writing Them

I have many notes.

DevOps notes. Job-search notes. AI research. Blog ideas. Guides. Projects. Half-finished thoughts. Good thoughts. Notes that were once good thoughts and are now mostly digital compost.

Obsidian is excellent for that because everything is Markdown, links and local control.

But a vault can slowly become a basement.

Not a cozy wine cellar.

More the kind of basement with a box labeled "important cables" from 2011 that you are afraid to throw out because it might contain the mini-USB cable that one day saves civilization.

The problem with a personal knowledge base is rarely that you cannot write more.

The problem is:

- What is still relevant?
- What is outdated?
- What connects?
- What lacks links?
- Which notes are just noise?
- Which new things on the internet are actually worth keeping?

That is where the graph becomes interesting.

## Graph Memory: Notes That Point

Obsidian already has a graph view. It is visually satisfying in the way a science-fiction control room is satisfying.

You see nodes, connections, clusters and lonely dots in the dark that clearly need either love or archiving.

But a graph is only useful if it is more than decoration.

So I made a small scanner that reads my Markdown files and builds local graph memory:

- title
- file path
- frontmatter
- tags
- aliases
- wikilinks
- incoming and outgoing connections
- missing metadata
- possible related notes

It writes the result to JSON and creates a human review note in Obsidian.

The important part is what it **does not** do:

It does not automatically rewrite the whole vault.

It does not delete notes.

It does not move things around with administrator rights and enthusiasm.

It just says:

> Here are 25 notes without good connections. Here are possible duplicates. Here are large notes without a hub link. Maybe have a look at them.

That is not full autonomy.

It is better than full autonomy.

It is an assistant with situational awareness.

## Self-Improving Does Not Mean Self-Glorifying

"Self-improving graph" can sound as if the system gets smarter at night while I sleep.

It does not.

And that is probably good.

What I mean is more sober:

1. The system scans the graph.
2. It finds weak spots.
3. It suggests improvements.
4. I or an AI session make small changes.
5. The next scan shows whether the graph improved.

It is a feedback loop.

Not magic.

Just a fairly grown-up way to use AI.

We know the same idea from software engineering:

- run tests
- read the failures
- make a small fix
- run again

I use the same principle on my knowledge.

If a note matters, it should be findable. If a research conclusion matters, it should be linked from a hub. If an old note has been replaced, it should be marked as superseded instead of whispering outdated advice from 2023.

## The Daily Research Scout

The second part is my daily research scout.

It scans sources such as:

- arXiv
- OpenAI
- GitHub Blog
- Microsoft Research
- Google Research
- Google News RSS searches around AI agents, computer science and quantum computing

It looks for topics I actually care about:

- AI agents
- coding agents
- MCP
- RAG and GraphRAG
- agent memory
- software engineering benchmarks
- DevOps and platform engineering
- security
- quantum computing
- AI governance

It creates three outputs:

1. A daily research briefing in Obsidian.
2. Candidate notes for things that look important.
3. Blog drafts if something has a public angle.

Again: it does not publish anything.

If an agent starts publishing your blog posts automatically, you are only a few prompts away from becoming a thought leader against your will.

And we do not want that.

Or maybe a little.

But not like that.

## How It Decides What Matters

The hard part is not finding news.

The internet is made of news. Most of it is repetition, product announcements wearing a tie, or "breakthroughs" that turn out to be a dropdown with AI in the name.

The hard part is filtering.

My scout uses a simple decision model:

- Does the topic match my core areas?
- Does it come from a reasonably credible source?
- Is it research, tooling or practice that can change how I work?
- Is it relevant to DevOps, platform engineering, AI agents or the blog’s technical profile?
- Is it merely interesting, or is it actually useful?

If something is lightly interesting, it goes into the briefing.

If it looks important, it creates a **research intake note** with `status: candidate`.

That word matters: candidate.

It means:

> This may be important. An adult still needs to look at it.

## The Blog As A Byproduct Of Learning

I want to write more.

But I do not want to write just to feed the algorithm another text about "5 ways AI changes everything".

My blog should come from actual work:

- something I built
- something I learned
- something I observed
- something that changed how I think about software, operations or AI

So the blog part of the scout is not a text machine.

It is an idea machine.

When it finds something relevant, it creates a draft with:

- source
- short angle
- possible structure
- relation to existing posts
- reminder to add my own judgment

It is a starting block, not the full race.

AI can help retrieve the ball.

It should not play the whole match and later explain that it has always been passionate about Danish technology policy.

## Why This Is Actually DevOps

This may sound like a personal productivity project.

It is.

But underneath, it is also very DevOps-like:

- clear input sources
- configuration
- automated daily run
- output as files
- review before promotion
- no automatic publishing
- small feedback loops
- clear guardrails
- local control

It is not enough to say: "AI, keep me updated."

That is a feeling, not a system.

A system requires answers:

- where should it look?
- what counts as relevant?
- what may it change?
- what must it not change?
- how do I see the result?
- how do I correct course?

Those are the same questions we should ask about any automation allowed to touch something important.

And notes are important.

Not because every note is brilliant.

Some of mine definitely are not.

But together they are context.

And context has become one of the most important resources in AI work.

## The Humble Use Of AI

There is a temptation to talk about AI as something enormous.

A new intelligence. A revolution. A machine that can do everything, right after the next release and with slightly better prompting.

My experience is more practical:

AI becomes most useful when you give it a small, clear job.

Not:

> Understand my whole life.

But:

> Find notes without links.

Not:

> Make me an AI expert.

But:

> Scan these sources every morning and show me the three things that might matter.

Not:

> Write my blog.

But:

> Make a draft with sources and an angle so I can write better and faster.

That is less spectacular.

It works.

And in software, "it works" is still an underrated feature.

## Conclusion

I increasingly believe in personal AI systems built as small platforms.

Not one giant chatbot.

But a collection of:

- notes
- scripts
- graph memory
- daily scouts
- review notes
- candidates
- blog drafts
- clear rules for what may happen automatically

It is not perfect.

It is not a replacement for reading, thinking and writing myself.

But it is a good scaffold.

Maybe that is how AI becomes most useful for ordinary developers:

Not as an all-knowing colleague with too much confidence.

But as a patient assistant that shows up every morning and says:

> I cleaned up the graph a little, found three papers and made a blog draft. You still have to make the coffee.

I can live with that.

## How The System Is Built

It is not a heavy platform. It is a set of small habits and files that make it easier to continue:

- Obsidian as a local knowledge base.
- Markdown notes with frontmatter, links and short answers at the top.
- Daily research scouts that create drafts instead of finished articles.
- Blog drafts that must be verified and given a human angle before publishing.
- Git and Hugo as the public publishing channel.

The most important thing is not the tool. The most important thing is that research, notes, job search and blog do not live in separate mental drawers. They can point to each other.

Read also:

- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)
- [DevOps Is Not a Pipeline](/karpov-blog/en/posts/devops-is-not-a-pipeline/)
- [EU AI Act in Practice: Transparency Is Not Just a Pop-up](/karpov-blog/en/posts/eu-ai-act-in-practice-transparency-is-not-just-a-popup/)
