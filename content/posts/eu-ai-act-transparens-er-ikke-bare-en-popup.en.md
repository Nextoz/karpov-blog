---
title: "EU AI Act in Practice: Transparency Is Not Just a Pop-up"
date: 2026-05-25
lastmod: 2026-06-07
slug: "eu-ai-act-in-practice-transparency-is-not-just-a-popup"
draft: false
translationKey: "eu-ai-act-transparens-er-ikke-bare-en-popup"
description: "The EU AI Act turns transparency into a practical product, DevOps and architecture problem. Here is what teams should start preparing now."
summary: "From 2 August 2026, Article 50 transparency rules in the EU AI Act begin to apply. That sounds legal, but in practice it is also about UI, metadata, logs, audit trails, tests and operations."
tags: ["AI", "EU AI Act", "DevOps", "Platform Engineering", "Regulation", "Compliance"]
categories: ["Technology Policy", "AI"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# EU AI Act in Practice: Transparency Is Not Just a Pop-up

The EU AI Act sounds like something you can park with Legal.

I think that is a mistake.

Not because lawyers should not be involved. They should. Preferably early, before someone builds an AI feature that sends personal data sightseeing through three SaaS products and an optimistic proof of concept.

But because transparency is not only legal text. It becomes a product problem, a UX problem, an architecture problem and eventually an operations problem.

And operations problems tend to land with the people who build, deploy and maintain systems.

## Why It Matters Now

On 8 May 2026, the European Commission published draft guidelines for the transparency obligations in Article 50 of the EU AI Act. The consultation is open until 3 June 2026.

The transparency rules themselves begin to apply from **2 August 2026**.

That is not a distant "one day we should probably" date. It is soon.

The rules are about informing users when they interact with certain AI systems and, in some cases, making AI-generated or manipulated content detectable through machine-readable markings.

The short version:

- If you use AI directly in the product, the user may need to know.
- If you generate synthetic text, audio, image or video, it may need marking.
- If you use emotion recognition or biometric categorization, people must be informed.
- If you publish AI-generated text on matters of public interest, you need to think carefully.

That may sound like compliance.

But anyone who has built software for more than ten minutes knows that "just inform the user" is rarely a tiny change.

## The Pop-up Trap

The easy version of transparency is a pop-up:

> This feature uses AI.

Now everyone is happy, right?

Legal has its text. Product has its modal. The developer got a ticket with the acceptance criterion "show label". Compliance can tick a box.

The problem is that the pop-up is often only the surface.

The real questions arrive afterwards:

- When should the message be shown?
- Who should see it?
- What does "the user interacts with AI" mean in our system?
- What if AI only assists an employee behind the scenes?
- What if the output is edited by a human?
- What if the content is exported to PDF, email or another system?
- Can we document afterwards that transparency was actually present?

This is where transparency stops being copy and starts being system design.

## Machine-Readable Marking Is Not Magic Dust

One of the more technical elements is machine-readable marking of AI-generated or manipulated content.

That sounds like something you can buy in a package:

> We just install watermarking, then we are done.

Maybe. Maybe not.

In practice, machine-readable marking can mean metadata, provenance, watermarking, API fields, content labels, audit logs or other mechanisms that make it possible to detect that something was AI-generated or manipulated.

Then come the boring, important questions:

- Where do we store the marking?
- Does it survive copy and paste?
- Does it survive export to PDF?
- Does it survive upload to a CMS?
- Does it survive when an integration transforms the data?
- How do we test that the marking still exists after the next release?
- Who owns the failure if a pipeline strips it away?

There is very little "just a pop-up" about that.

## Transparency Should Be Testable

If transparency is a requirement, it should be testable.

Otherwise it is not a requirement. It is an intention with nice typography.

Examples:

- UI tests that verify AI labels in relevant flows
- API tests that verify metadata on AI-generated content
- integration tests that verify labels survive export or forwarding
- log tests that verify AI-related events are traceable
- deployment checks that catch missing configuration
- runbooks that explain what support should answer when a user asks

The best compliance solutions are often boring in the right way. They live in pipelines, tests, logging, documentation and release processes. Not in a panicked Confluence page written the night before an audit.

## The DevOps Angle

AI governance is often discussed as if it happens in a meeting room with PowerPoint and serious faces.

In practice, much of the work lands in systems.

If a product team uses AI in production, someone should be able to answer:

- Which environments have AI features enabled?
- Which models, services or vendors are used?
- Which secrets and API keys exist?
- Which data is sent to the model?
- Which logs show AI-related events?
- Which dashboards show error rate, latency and dependency failures?
- Which deployment gates protect labels, logs or metadata from disappearing?
- What is the rollback plan if an AI feature behaves badly?

This is not only Legal. It is platform engineering.

It is CI/CD. It is observability. It is access control. It is documentation. It is incident response. It is product responsibility with work boots on.

## Four Types Of AI, Four Kinds Of Questions

Teams should not treat all AI features the same.

I would start with a simple split:

### 1. Internal AI Assistance

Example: a developer assistant, internal documentation bot or employee support tool.

Questions:

- Which internal data may it use?
- Are prompts and answers logged?
- Can employees accidentally enter personal data or secrets?
- Should output be marked if it is later sent to customers or citizens?

### 2. User-Facing AI Interaction

Example: chatbot, search assistant, advice flow or customer support.

Questions:

- Does the user know they are interacting with AI?
- Can the user reach a human?
- Is there a clear boundary between information, recommendation and decision?
- How are errors and hallucinations handled?

### 3. AI-Generated Content

Example: text, images, video, audio, summaries, reports or product descriptions.

Questions:

- Should the content be marked?
- Is there human editorial control?
- Who takes responsibility for publishing?
- Does the marking survive when content moves between systems?

### 4. AI-Assisted Decisions

Example: screening, prioritization, risk assessment or case handling.

Questions:

- Is the system high-risk?
- Is a user or citizen affected by the output?
- Can the decision be explained?
- Where is human control?
- Which audit trails exist?

This is not a complete legal classification. It is a practical start.

And it is better than "we just use a bit of AI here and there."

## A Practical Checklist For Danish Teams

If I sat in a Danish product, DevOps or platform team, I would start here:

1. Make an AI inventory.
2. Put an owner on every AI feature.
3. Decide where transparency lives: UI, API response, metadata, database, logs, export format, documentation or support material.
4. Make it testable.
5. Write a runbook.
6. Build audit trails without logging everything indiscriminately.

Auditability does not mean "store everything forever".

It means storing enough to understand, explain and troubleshoot the system without creating a new privacy problem.

That requires balance:

- What should be logged?
- What should be masked?
- How long is it retained?
- Who may read it?
- How is it deleted?

This is where DevOps, security, product and legal should talk to each other, preferably before production starts the conversation for them.

## What This Means For Senior Developers

I think AI makes the senior role more important, not less.

Not because senior developers need to memorize every paragraph of the EU AI Act. That would be a sad superpower.

But because seniors often sit close to the decisions where law becomes architecture:

- Should AI output be stored?
- Should it be reproducible?
- What do we log?
- How do we distinguish model errors from ordinary application errors?
- How do we avoid sending sensitive data to the wrong place?
- How do we build approval flows without killing productivity?
- How do we make sure transparency does not disappear in the next refactor?

This is where experience matters.

Not as the person who says no to everything, but as the person in the room who has seen enough systems break to ask:

> Okay, but how does this work Monday morning when support gets the first case?

## My Position

I am fundamentally positive about AI.

But I am even more positive about AI that can be operated, explained, tested and maintained.

If transparency becomes a pop-up nobody reads, we have not gained much.

If transparency is designed into systems as metadata, UI, logs, tests, runbooks, ownership and audit trails, it can become part of trust infrastructure.

That may not be the most glamorous sentence in the world.

But in production, trust infrastructure beats demo magic almost every time.

## Read Also

- [DevOps Is Not a Pipeline](/karpov-blog/en/posts/devops-is-not-a-pipeline/)
- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)
- [Project Glasswing](/karpov-blog/en/posts/project-glasswing/)
- [Portfolio: DevOps, Platform Engineering and .NET](/karpov-blog/en/projects/)

## Sources

- [European Commission: draft guidelines on transparency obligations under Article 50](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act)
- [European Commission: consultation on transparency obligations under the AI Act](https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act)
- [AI Act Service Desk: EU AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act)
