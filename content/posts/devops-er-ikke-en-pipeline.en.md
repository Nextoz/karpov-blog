---
title: "DevOps Is Not a Pipeline"
date: 2026-05-22
lastmod: 2026-06-07
slug: "devops-is-not-a-pipeline"
draft: false
translationKey: "devops-er-ikke-en-pipeline"
description: "A short practical note about DevOps, CI/CD, observability, rollback and documentation. DevOps is not just YAML with confidence."
summary: "DevOps is not just a pipeline. It is the ability to move software safely from idea to operations, detect problems quickly and fix them without panic."
tags: ["DevOps", "Platform Engineering", "CI/CD", "Observability", "Azure DevOps", "Kubernetes"]
categories: ["DevOps", "Platform Engineering"]
author: "Evgeny Karpov"
ShowReadingTime: true
---

# DevOps Is Not a Pipeline

![A stylized pipeline with the text: This is not DevOps.](/karpov-blog/images/this-is-not-devops-pipeline.svg)

There is a special kind of optimism that appears when someone says:

> "We have DevOps. We have a pipeline."

That is a little like saying you have a kitchen because you own a spoon.

A pipeline is good. I love a pipeline that builds, tests and deploys without requiring incense, tribal knowledge and one specific developer named Brian.

But DevOps is not just YAML with confidence.

DevOps is the work that makes software **deliverable, operable and understandable**.

## The Short Version

A good DevOps flow answers five questions:

- Can we build the same artifact again?
- Can we test the change fast enough to dare merging it?
- Can we deploy without manual ceremony?
- Can we see whether the system is healthy afterwards?
- Can we roll back when reality gets creative?

If the answer is no, you do not have one DevOps problem.

You have five DevOps problems in a trench coat.

## Start With Feedback

The most important property of a pipeline is not that it looks nice.

It is that it gives feedback quickly enough for someone to still remember what they were doing.

Build. Test. Security scan. Package. Deploy to an environment that resembles reality enough not to be theater.

If feedback arrives two days later, it is not feedback. It is archaeology.

DORA points to the same basics again and again: small changes, automated tests, deployment automation, version control and observability. Not because they sound modern, but because they reduce the risk of changing software.

## Make Deployment Boring

The best deployment is not the heroic deployment.

The best deployment is the one where nobody has to write "just five minutes, I am deploying" in Slack with the kind of energy that makes everyone hold their breath.

Boring deployments require:

- the same build artifact through environments
- configuration without secret manual clicks
- migrations that have been thought through
- feature flags or another way to control risk
- a rollback plan before rollback becomes poetry

Release engineering is about reproducibility, automation and traceability. It sounds dry. That is the point. Production rarely rewards drama.

## Observability Is Not Decoration

Logs, metrics and traces are not something you sprinkle onto the system afterwards.

They are part of the design.

When something fails, the team should be able to answer:

- What happened?
- Which version is running?
- Which dependencies are failing?
- Where did latency increase?
- Which users or jobs are affected?

If the answer is "we will check three portals and ask Anders", the system is not observable. It is just socially distributed logging.

OpenTelemetry’s basic idea is to collect signals such as traces, metrics and logs so we can understand system behavior across boundaries. It is not magic. It is better breadcrumbs.

## Documentation Is Operations Too

The most underrated DevOps discipline is documentation.

Not 80 pages in Confluence that nobody has touched since Java 8 was young and hopeful.

Short notes:

- how we deploy
- how we troubleshoot
- how we rotate secrets
- how we read the dashboard
- how we roll back
- how we know everything is normal

A good runbook is not literature. It is a fire instruction for tired software.

## My Practical Checklist

If I had to improve a DevOps flow tomorrow, I would start here:

1. Find the most painful manual release task.
2. Make it visible in the pipeline or documentation.
3. Add a quick test that catches the most embarrassing failure.
4. Make deployments leave a trace: commit, version, environment and time.
5. Create a dashboard that shows user-perceived health, not only CPU fitness.
6. Write a rollback note while everything is calm.
7. Repeat without calling it a transformation.

The last point matters.

If every improvement requires a transformation, the organization eventually becomes allergic to improvement.

## Conclusion

DevOps is not about having the most tools.

It is about making change less dangerous.

A good pipeline helps. Kubernetes can help. Azure DevOps can help. Observability can help. AI will probably help even more.

But only if the system around the tools is understandable.

DevOps is not a pipeline.

DevOps is the ability to change software without everyone in the room instinctively looking at the same poor person.

Read also:

- [AI Is No Longer a Chatbot](/karpov-blog/en/posts/ai-is-no-longer-a-chatbot/)
- [EU AI Act in Practice: Transparency Is Not Just a Pop-up](/karpov-blog/en/posts/eu-ai-act-in-practice-transparency-is-not-just-a-popup/)
- [Project Glasswing](/karpov-blog/en/posts/project-glasswing/)
- [Portfolio: DevOps, Platform Engineering and .NET](/karpov-blog/en/projects/)

## Sources

- [Wikipedia: The Treachery of Images](https://en.wikipedia.org/wiki/The_Treachery_of_Images)
- [DORA: Continuous delivery](https://dora.dev/capabilities/continuous-delivery/)
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/)
- [OpenTelemetry: Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
