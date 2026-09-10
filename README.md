# Duck-mode 🦆

**An agent skill that helps you think without taking over the thinking.**

> We spent years making AI better at answering developers. Maybe we also need a mode that refuses to.

Duck-mode gives an assistant a different job: help you navigate your reasoning. It reveals
connections, tests assumptions, follows side paths, and brings in evidence. Your opening
question is a starting point; reaching a decision is one possible destination.

> **Models can change. The thought history cannot.**

That is a design principle: preserve what you said, what the assistant suggested, and how
the conversation got here. Duck-mode defines an explicit thought-state model with provenance,
traveled paths, and branch state, which the model maintains within the available conversation
context. The current skill does not implement durable storage or enforce state transitions
in code, and therefore cannot guarantee continuity across model switches. A new session
needs the relevant history supplied to it.

## Try it

With the skill installed:

```text
$duck-mode

I'm thinking about whether this project should live
under my company or my personal GitHub.
```

You can also paste [the portable prompt](prompts/generic.md) into a chat or supported
custom-instruction field, then explicitly request Duck-mode. No app or backend is required.

## A short conversation

*An illustrative conversation, not a recorded model evaluation.*

**You:** Should this project live under my company or my personal GitHub?

**Duck:** 🔎 What do you want someone to understand about you when they find it?

**You:** That I can design AI systems, not just write prompts.

**Duck:** ↗ Imagine an engineer spends 90 seconds looking at the repository.
What would you want them to notice that they wouldn't expect from a prompt repo?

```text
🎯 Company or personal GitHub? → engineering credibility ← 🦆
                                  └─ · a reader's first encounter
```

**You:** Actually, I care less about impressing them than making a failure visible:
the assistant slowly starts doing all the thinking.

**Duck:** 🔗 The project could make that handover visible. That shifts the question
from how people see you to what they can notice in their own conversations.

```text
🎯 Company or personal GitHub? → engineering credibility → ownership drift ← 🦆
                                                           └─ · noticing the handover
```

**You:** Yes—the moment a suggestion starts being treated as something I said.
That's what I want to demonstrate.

**Duck:** 🪞 A suggestion changing owners without anyone noticing. You have a concrete
moment to explore.

See [the worked examples](skills/duck-mode/references/examples.md) for evidence retrieval,
corrections, closed branches, and reconnecting earlier ideas.

## What makes it different

- **Thought state and provenance.** Keep track of who introduced an idea, what is tentative,
  and which paths were actually explored. Agreement does not erase authorship.
- **Reasoning ownership.** The assistant can contribute surprising ideas without building
  your conclusion through a chain of confirmations.
- **Branching exploration.** Follow connections, return to earlier paths, or discover a
  different question. The Thought Window shows the route rather than a decision checklist.
- **Evidence Gate.** Retrieve material facts with available tools, identify their sources,
  and show what they change. State the limitation when verification is unavailable.
- **Explicit exits.** `stop duck-mode` stops; `give me your conclusion` exits and requests
  an answer; `summarize` preserves the reasoning without adding a recommendation.

## How it works

```text
User thought + available evidence
               ↓
Update thought graph and provenance
               ↓
Choose a useful move
               ↓
Reveal terrain / update navigation
               ↓
Thought Window + question or observation
               ↓
User follows, reshapes, rejects, or stops
```

The model performs these steps under a behavioral contract. The skill defines the
interaction protocol; the host supplies the model, conversation context, and tools.
State management should produce natural conversation, not narration about internal rules.

## Status

**Experimental / v0.1 skill package.** The behavioral specification has its own v1.1 label.
Expect the protocol to evolve as real conversations expose weaknesses.

The repository includes 114 synthetic regression cases and a manual evaluation workflow.
CI validates the package and test fixtures; it does not establish behavioral reliability.
No cross-model evaluation results or automatic state-persistence guarantees are claimed.

## Installation

Download `duck-mode.zip` and `duck-mode.zip.sha256` from this repository's GitHub Releases
page once a main-branch build has published, or build them locally with the commands below.
You can also copy the complete [skills/duck-mode](skills/duck-mode/) directory into your
host's skills directory.

Extract the archive and place its single `duck-mode/` folder directly under that directory.
Follow the host's reload procedure, then invoke `$duck-mode`. For hosts using named
invocation, request Duck-mode explicitly. On hosts honoring `allow_implicit_invocation: false`,
the skill activates only when explicitly invoked.

Verify downloaded assets from their directory:

```sh
sha256sum -c duck-mode.zip.sha256
```

The installable package contains only:

```text
duck-mode/
├── SKILL.md
├── LICENSE
├── agents/openai.yaml
└── references/examples.md
```

The full behavioral contract is in `SKILL.md`. Examples are an optional reference.
The skill has no runtime dependencies or bundled credentials; evidence retrieval uses
whatever tools its host provides. This repository README stays outside the skill archive.

### Build the package

```sh
python scripts/build_skill.py
python scripts/build_skill.py --check
```

The builder copies the contract from `prompts/generic.md` byte-for-byte and writes the
skill folder, `dist/duck-mode.zip`, and its checksum. It never writes the prompt.
Generated release archives are ignored by Git.

## Repository layout

| Path | Purpose |
| --- | --- |
| [SPEC.md](SPEC.md) | Canonical behavior and regression-case definitions |
| [prompts/](prompts/) | Portable and host-oriented prompts sharing that contract |
| [skills/duck-mode/](skills/duck-mode/) | Installable skill and optional examples |
| [scripts/](scripts/) | Prompt extraction, packaging, and manual eval tooling |
| [tests/](tests/) | Build and evaluation-pipeline tests |
| [evals/](evals/) | Synthetic fixtures and behavioral scoring rubrics |
| [examples/](examples/) | Additional behavior illustrations |

The repository is the source for development and contribution. Release ZIPs contain only
the skill needed for installation.

## CI and releases

Pull requests and `main` builds validate generated artifacts, tests, packaging, and checksums.
Successful `main` builds publish a uniquely tagged prerelease containing `duck-mode.zip`
and its SHA-256 checksum. Reruns leave published releases unchanged.

CI does not run provider/model behavioral evaluations.
See [the release pipeline](.github/workflows/release.yml) for details.

## Developing and evaluating

`SPEC.md` is the source of truth. Prompt generation extracts its behavioral contract;
eval generation separately extracts its cases, keeping test answers out of prompts.
Skill packaging then consumes the existing generic prompt:

```text
SPEC.md → prompts/generic.md → skills/duck-mode → dist/duck-mode.zip
        └→ evals/eval_cases.json
```

For intentional behavior changes, edit the specification and regenerate the affected
artifacts. These development commands can change the generic prompt:

```sh
python scripts/build_prompts.py
python scripts/build_tests.py
python scripts/build_skill.py
```

Use the skill-only build when packaging existing behavior. See [the evaluation guide](evals/README.md)
for replay instructions, evidence profiles, and the D01–D24 rubric. The manual runner
prepares inputs or records replies; it does not call a model or assign passing scores.

## Author

Created by [Radu (rvulpescu)](https://github.com/rvulpescu).

I'm a software architect interested in how we design AI systems that augment human
reasoning without quietly replacing it.

## License

[MIT](LICENSE).
