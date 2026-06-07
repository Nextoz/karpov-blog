---
title: "AI Agents Need Memory"
date: 2026-06-06
lastmod: 2026-06-07
slug: "ai-agents-need-memory"
translationKey: "ai-agenter-skal-bruge-hukommelse"
draft: false
description: "A practical note on why AI agents need not only APIs, but also memory, sources, validation and human review."
summary: "APIs give AI agents access to systems. Memory determines whether they can work responsibly over time without repeating mistakes, losing context or inventing a beautiful explanation afterwards."
tags: ["AI", "AI Agents", "Agent Memory", "DevOps", "Platform Engineering", "Observability"]
categories: ["AI", "DevOps"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# AI Agents Need Memory

I recently wrote that AI agents need APIs.

I still think so.

But APIs are only half the problem.

An agent that can call an API can do something in the world. It can fetch data, create a pull request, change configuration, write a comment or start a process.

That is useful.

It is also where the problems begin.

If the agent cannot remember why it did something, which sources it used, which checks failed, which decisions a human already made and where the boundary of the task is, you have not gained a colleague.

You have gained a very fast intern with amnesia and production access.

That sounds like a joke.

Mostly, it is an incident waiting to happen.

## Memory Is Not Chat History

Many people still think of AI memory as a longer conversation.

That is too narrow.

For real AI agents, memory is not only about remembering what the user wrote five minutes ago. It is about working with state over time.

A useful agent needs to remember:

- the goal of the task
- which files, systems and sources it used
- which assumptions it made
- which checks were run
- what failed
- what it has already tried
- which decisions a human approved
- which parts of the work are still uncertain

That is not romantic AI.

It is ordinary software engineering.

And that is exactly why it matters.

## Unstructured Context Quickly Becomes Noise

A large context window can feel like a solution.

Just give the model more text. More files. More notes. More logs. The whole repository. The whole documentation set. The entire organization’s collective guilty conscience in Markdown.

The problem is that more context does not automatically create more understanding.

Sometimes it just gives the agent more opportunities to find the wrong detail and sound confident while doing it.

That is why I think agent memory is a system problem, not only a model problem.

Memory needs structure:

- What is a fact?
- What is a decision?
- What is a temporary assumption?
- What is an old note?
- What is a source?
- What is a validated change?
- What still needs review?

If everything is just text in one large pile, the agent does not necessarily become smarter. It becomes better fed.

And anyone who has worked with old documentation folders knows that well-fed confusion is still confusion.

## My Small Version: Obsidian As Agent Memory

I have used my own Obsidian vault as a small laboratory for this.

Not as a grand product. More as a practical experiment:

Can notes, research, tasks, skills and links become useful for AI agents over time?

The short answer is yes.

But only if the notes are written to be used again.

A note that is just a text dump helps less. A note with a short conclusion, frontmatter, sources, status, related notes and a clear link to a hub is much more valuable.

That sounds small.

It is not.

When an agent starts a task, it needs to find the right context without reading my whole digital attic first.

So I have started treating notes as small memory objects:

- `type`: research, guide, skill, dashboard or reference
- `status`: active, draft, archived or superseded
- `memory`: semantic knowledge, procedure or episodic log
- `confidence`: how reliable the note is
- `source`: where the information came from
- `related notes`: where it belongs in the graph

YAML is not magic.

The point is that the agent needs to sort.

## Remembering And Proving

An agent should not only remember.

It should be able to show why it believes something.

This is where software engineering and AI governance meet naturally.

If an agent changes code, we should be able to see:

- what it changed
- why it changed it
- which tests were run
- which tests were not run
- which files it touched
- which requirement it tried to satisfy
- which risks remain

That is very close to ordinary pull request discipline.

Maybe that is the point.

The best agent memory is not a mysterious AI ability. It is a combination of good notes, good logs, clear tasks, tests, review and a little humility.

In other words: all the boring things that usually save software projects once the demo is over.

## Longer-Running Agents Need Operations

OpenAI, Microsoft and GitHub are all moving toward agents that work longer and closer to real workflows.

That may be coding agents in GitHub, agentic development in Warp, enterprise context in Microsoft 365, or background tasks that do not just answer in a chat but actually try to complete work.

That changes the risk picture.

A chatbot that answers incorrectly is annoying.

An agent that works incorrectly for hours with access to tools, repositories and internal data is something else.

So the old DevOps questions become very modern again:

- What may run automatically?
- What requires review?
- Where are the logs?
- How do we detect errors?
- How do we stop the process?
- Who owns the change?
- What happens when the agent meets an unclear instruction?

It is not enough for the agent to be intelligent.

It also needs to be operable.

## Agent-Ready Means Memory-Ready

Many teams will talk about whether their systems are agent-ready.

That is a good question.

But it should not only be about APIs.

An agent-ready system also needs to be memory-ready:

1. Documentation must be current enough to use.
2. Decisions must be visible.
3. System boundaries must be clear.
4. Tests and checks must run without drama.
5. Logs must explain both human and agent-driven actions.
6. Tasks must have clear stop conditions.
7. Important knowledge must be findable again.

If that sounds like good platform engineering work, it is because it is.

AI does not make old discipline problems less important.

It makes them more visible.

## Conclusion

AI agents need APIs.

But they also need memory.

Not just as a long chat log, but as structured working memory with sources, decisions, status, validation and review.

Otherwise we get agents that can act without being able to explain themselves.

That is a bad combination.

The next big AI task inside companies will not only be buying more agents.

It will be building environments where agents can work without making the systems more unclear.

It is about context.

It is about operations.

It is about memory.

And yes, unfortunately, it means documentation still matters.

Sorry.

Read also:

- [AI Agents Need APIs](/karpov-blog/en/posts/ai-agents-need-apis/)
- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)
- [DevOps Is Not a Pipeline](/karpov-blog/en/posts/devops-is-not-a-pipeline/)
- [My Obsidian Vault Got a Small Research Department](/karpov-blog/en/posts/my-obsidian-vault-got-a-small-research-department/)

## Sources

- [OpenAI: Warp's big bet on building open source with GPT-5.5](https://openai.com/index/warp/)
- [OpenAI: Codex for almost everything](https://openai.com/index/codex-for-almost-everything/)
- [Microsoft: AI alone won't change your business. The system running it will.](https://blogs.microsoft.com/blog/2026/06/02/ai-alone-wont-change-your-business-the-system-running-it-will/)
- [GitHub Changelog: Copilot CLI improved UI, rubber duck, prompt scheduling and voice input](https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/)
- [arXiv: Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448)
- [arXiv: Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](https://arxiv.org/abs/2606.06036)
