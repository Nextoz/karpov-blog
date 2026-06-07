---
title: "AI Agents Need APIs"
date: 2026-06-04
lastmod: 2026-06-07
slug: "ai-agents-need-apis"
translationKey: "ai-agenter-skal-bruge-api-er"
draft: false
description: "A short note on why AI agents quickly become an API, governance and platform engineering problem."
summary: "Postman, Microsoft and OpenAI all point in the same direction: AI agents do not only need better models. They need to work against real systems with context, access control, logs and clear boundaries."
tags: ["AI", "AI Agents", "APIs", "DevOps", "Platform Engineering", "Governance"]
categories: ["AI", "DevOps"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# AI Agents Need APIs

AI agents have run into a very ordinary software problem:

They need APIs.

That sounds dry. That is also the point.

Postman has launched an AI Engineer that can work with API design, root-cause analysis and PR checks. Microsoft is preparing Work IQ APIs for Microsoft 365, so agents can retrieve business context and act through fewer, more agent-friendly tools. OpenAI is moving Codex deeper into enterprise workflows and AWS.

Those are three different product stories.

But they point to the same shift:

AI is getting an integration surface.

## The New Bottleneck Is Context

The first wave of AI discussion was mostly about the answer.

Can the model write code? Can it explain the error? Can it make a plan?

That still matters. But in real systems it is rarely enough.

An agent that helps with software needs to know more than what a good function looks like in isolation. It needs to understand contracts, dependencies, naming, ownership, environments, data, permissions and the strange local rules that are not in the documentation but still govern half the system.

Postman calls part of this problem context debt. That is a useful phrase.

When agents can produce more code, more tests, more changes and more suggestions, the need for shared system understanding grows too. Otherwise you do not get faster software development. You get faster confusion with nicer commit messages.

## From Chatbot To Platform Surface

The interesting part of the new agent announcements is not just that the tools are getting smarter.

It is that they are being connected to the places where work already happens:

- API catalogs
- pull requests
- sandboxes
- documentation
- Microsoft 365 data
- enterprise cloud environments
- existing governance and security models

That changes the question.

It is no longer only:

> How good is the model?

It is also:

- Which endpoints may the agent call?
- Which credentials does it get?
- What runs in a sandbox?
- What requires human approval?
- Where are actions logged?
- Who owns the contract?
- How do we discover that the agent misunderstood the system?
- How do we roll back?

Those questions do not make the prettiest keynote slides.

They do decide whether the technology can be used without creating a new operations problem.

## The Agent Era Is Platform Work

I think many companies will underestimate this.

They will ask:

> Which agent should we buy?

A better question may be:

> Which platform will the agent land in?

If the APIs are unclear, permissions are messy, documentation is old and nobody knows who owns what, the agent does not become wise just because it gets access.

It becomes another user of an unclear system.

Good internal platforms become more valuable in this world. Clear API contracts, operational documentation, observability, security boundaries and good review processes are not only useful for humans. They become the foundation agents work on.

Agent-ready software looks a lot like the software we should already have been building.

Just with less tolerance for mess.

## My Short Checklist

If a team wants to prepare for AI agents, I would start very practically:

1. Identify the most important internal APIs.
2. Make ownership and contracts explicit.
3. Make sure logs can explain both human and agent-driven actions.
4. Use sandboxes for anything that can change state.
5. Require human approval for irreversible or risky changes.
6. Test agent suggestions like any other change.
7. Write runbooks before the first agent is allowed to "help" anywhere near production.

That may sound conservative.

Fine.

Production is a conservative place. It does not reward enthusiasm alone.

## Conclusion

AI agents will not only be an AI problem.

They will be an API problem, a governance problem and a platform engineering problem.

That is actually good news.

It means the next phase of AI is not only about choosing the right model. It is about building the right frame around it.

Who may the agent talk to?

What may it do?

How do we see what happened?

And how do we stop it again?

If those questions are handled, agents become much more interesting.

If not, we get automation on top of ambiguity.

And software has, to be fair, plenty of experience with that already.

Read also:

- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)
- [DevOps Is Not a Pipeline](/karpov-blog/en/posts/devops-is-not-a-pipeline/)
- [EU AI Act in Practice: Transparency Is Not Just a Pop-up](/karpov-blog/en/posts/eu-ai-act-in-practice-transparency-is-not-just-a-popup/)

## Sources

- [Postman: Introducing the AI Engineer](https://blog.postman.com/introducing-the-ai-engineer/)
- [Microsoft 365 Blog: Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)
- [OpenAI: OpenAI frontier models and Codex are now available on AWS](https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/)
- [OpenAI: Codex for every role, tool, and workflow](https://openai.com/index/codex-for-every-role-tool-workflow/)
