# Security Policy

## Scope

This repository contains public documentation, diagrams, examples, and non-destructive audit scripts for `chudi.dev`.

This policy covers:

- vulnerabilities in repository code or workflows
- unsafe handling of credentials or secrets in the repo
- inaccurate or dangerous automation behavior in repository scripts

This policy does not guarantee response for vulnerabilities in third-party services referenced by the docs.

## Reporting a Vulnerability

Email `hello@chudi.dev` with the subject line `Security report: ai-visible-web-architecture`.

Include:

- a concise description of the issue
- reproduction steps
- impact assessment
- suggested remediation if you have one

Please do not open public issues for undisclosed security findings.

## Response Expectations

- Initial acknowledgement target: within 5 business days
- Triage target: within 10 business days
- Public disclosure: after remediation or coordinated disclosure agreement

## Secure Contribution Rules

- Never commit secrets, tokens, or private keys.
- Keep scripts network-read-only unless a change is explicitly scoped and documented.
- Prefer standard-library or pinned tooling for verification workflows.
- Document any new external action or automation used in CI.
