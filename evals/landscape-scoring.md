# Trail, current location, visible terrain

Four synthetic `landscape-*` probes test three map classes, unvisited terrain versus belief,
provenance as annotation, and compression with a meaningful return. No model results exist.

Inspect the actual map, not just presence of icons. → denotes traveled transitions, ← 🦆
(or “You are here”) marks current location, · denotes grounded unvisited terrain, and ↩
marks a supported return. ? belongs to an uncertain relationship; a dot is not an unknown
answer, assumption, requirement, or established fact. A future landmark must not appear
as already visited. Ground nearby terrain in the supplied context; do not fill a quota.

Distance-from-origin and analytical Frontier panels are retired. The historical
navigation-topology-and-distance case ID remains stable, but its acceptance criteria now
follow the landscape contract. Existing worked golden maps have been updated accordingly.
Do not reward a status ledger merely because it has a trail label at the top.

One compact map retains the original and traveled order, with grouped historical hops or
explicit elision when necessary. Nearby and return landmarks count toward the normal
five-landmark budget; repeated references do not create extra concepts. A compressed path
must not be used to hide a long unordered inventory. User-requested larger maps remain valid.

Provenance stays enforceable in prose. Source reads are mandatory for the evidence probe;
removing 📚 from a node is not permission to omit citations, imply independent verification
of user inputs, or invent factual properties. Use status annotations only where they explain
topology. Preserve original assistant authorship of solution possibilities after adoption.
