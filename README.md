The control-plane skill pack: one canonical procedure home that routes a request to the minimum skill bundle, with the gate table and failure policy.

# protean-control-plane

The control-plane ingredient of the Protean Kit distribution. It holds one
canonical procedure home: a trigger index that routes a request to the minimum
skill bundle, the dispatch preflight, the GitHub workflow, the failure policy,
and the table of gates the plane cites.

## Do you need this?

ROLE: One canonical procedure home for dispatch. A trigger index routes each request to the minimum skill bundle, with the dispatch preflight, the GitHub workflow, the failure policy, and the table of cited gates.

USE WHEN:
- A coordinator or relay must load only the bundle a task names, starting from `skills/protean-control-plane/SKILL.md` as the routing screen.
- Record gates must run through one wrapper that locates the installed `protean-ops` ingredient and reports each cited gate unavailable with exit 0 when it is absent.

SKIP WHEN:
- `protean-doctrine` or `protean-ops` is missing and cannot be installed. The manifest declares both as hard requirements and the plane ships no copy of either file, so `--no-deps` installs report degraded.
- The need is platform mechanics or supervision and recovery detail. This README states the skill deliberately omits them because their documents are outside this distribution.

## What it installs and where

| Path | Contents |
|---|---|
| `skills/protean-control-plane/` | the control-plane procedure skill |
| `gates/protean-control-plane/` | the wrapper that runs the cited record gates, the leak gate, and the blocklist |

## Install

```bash
bash install.sh --target <dir>
bash install.sh --target <dir> --dry-run
```

Bash and coreutils only, zero network calls, every written path printed, and no
`--target` means no run. A dry run writes nothing.

Installs alone with this command, resolving only its required dependencies listed
in its manifest entry. Optional relationships are reported, not fetched.

## Requirements and recommendations

Requires `protean-doctrine` and `protean-ops`. The trigger index cites the
doctrine, and the gate table cites the ops gates by their ingredient-relative
paths; this ingredient declares those two as hard requirements and ships no copy
of either file. Recommends `protean-drafts`, `protean-github-flow`, and
`protean-sym2p`.

Installed alone, exactly three repositories are written: `protean-doctrine`,
`protean-ops`, and this one. With `--no-deps`, exactly one is written and the two
requirements are reported as `degraded`.

## Use

Read `skills/protean-control-plane/SKILL.md` first. It is the routing screen: load
the one bundle a request names, not every skill.

## Gates

| Gate | Command (declared) |
|---|---|
| internal-name gate | `python3 gates/protean-control-plane/check-internal-names.py .` |
| control-plane gates | `python3 gates/protean-control-plane/check-control-plane-gates.py` |

The wrapper locates the ops ingredient and runs its gates, including the
contribution-state gate (G-14). When the ops ingredient is not installed beside
it, each cited gate is reported `unavailable`
and the wrapper exits 0: degraded mode is reported, never hidden, and never
faked. Tests cover both paths.

## Offline and cache behaviour

Used through the composer, this ingredient is fetched once from its pinned tag
and reused from a content-addressed cache keyed by commit SHA. `--offline`
performs zero network calls and fails closed when the cache entry is absent.

## Limits and open items

The skill deliberately does not restate platform mechanics or supervision and
recovery steps, because the documents that carry them are not part of this
distribution. The control plane cites the record gates rather than carrying them,
which is why the dependency is hard. Section G states the rule for contribution
mode and carries no counter: the bounded values, the toggle's value, and the
counters live in the contribution-state record under the ops ingredient, so a
reader of this skill learns what is permitted and the gate decides what is
allowed. No unresolved item is carried by this
ingredient; the open items of the protocol live in `protean-sym2p`.

## License

MIT. The committed `LICENSE` file is authoritative.
