# Module 7 — Look at the Architecture: What's the Gap? Intro GitOps & ArgoCD 

**Goal:** Step back, look at the full pipeline students just built with their own hands, name its weaknesses precisely, and introduce GitOps/ArgoCD as the direct answer. Short and theory-only — the payoff is the hands-on in Module 8.

## 1. Draw the architecture they built (5 min)

```
Git (app-repo) → GitLab CI (build) → Registry → GitLab CI (deploy) → Cluster
                                                        ▲
                                              holds KUBE_CONFIG here
```

## 2. Push vs Pull (5 min)

- **Push (all of today so far):** an external actor (you, or CI) reaches *into* the cluster. Requires giving that actor cluster credentials.
- **Pull (GitOps):** an agent *inside* the cluster watches Git and reaches *out* to read it, then reconciles the cluster to match. No external actor needs cluster credentials.

## 3. GitOps principles (5 min)

- Git is the **single source of truth** for desired state — this is exactly why `manifests-repo`/the Helm chart mattered all day.
- Everything declarative (which Module 3 and 4 already set up).
- An automated agent continuously reconciles actual state → desired state.
- Drift is detected and can be automatically corrected ("self-healing").

## 5. What ArgoCD is, concretely (5 min)

- A controller running **inside** the Kubernetes cluster.
- You define an `Application` custom resource telling it: which Git repo/path to watch (their Helm chart in `manifests-repo`), which cluster/namespace to deploy to, and the sync policy (manual or automated, self-heal on/off, prune on/off).
- It continuously diffs live cluster state vs. Git, showing **Synced/OutOfSync** and **Healthy/Degraded**.

Draw the reconciliation loop:
```
  ┌────────────┐        watches         ┌───────────────┐
  │ manifests  │ ─────────────────────▶ │    ArgoCD      │
  │   repo     │                        │  (in-cluster)  │
  │ (Helm chart│ ◀───── diffs against ─ └───────┬────────┘
  │  built in  │                                 │ applies/corrects
  │  Module 4) │                                 ▼
  └────────────┘                         ┌───────────────┐
                                          │   Cluster      │
                                          └───────────────┘
```

Emphasize: this loop runs **continuously**, not just once per commit like the Module 6 pipeline.

## Bridge line into Module 8

"You already built the Helm chart ArgoCD needs, in Module 4. You already pushed it to `manifests-repo`. The only new thing now is *who* deploys it — instead of you, or a CI job, it'll be ArgoCD, watching."
