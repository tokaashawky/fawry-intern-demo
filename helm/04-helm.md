# Module 4 — Helm: Template It, Deploy Manually
## Steps for students

1. Look at the provided chart skeleton in `helm/flask-app/`:
   - `Chart.yaml` — chart metadata
   - `values.yaml` — the knobs: `image.repository`, `image.tag`, `appVersion`, `appColor`, `deployedBy`
   - `templates/deployment.yaml`, `templates/service.yaml` — same YAML as Module 3, but with `{{ .Values.xxx }}` placeholders
2. Compare side by side with `manifests/deployment.yaml` from Module 3 — point out it's the *same* resource, just parameterized.
3. Set `deployedBy: "manual-helm"` and the right image repo in `values.yaml`.
4. Install:
   ```bash
   helm install flask-app .
   ```
5. Check the browser — page now says `manual-helm`.
6. Simulate a version bump using `--set` instead of editing files, to show Helm's parameterization value:
   ```bash
   helm upgrade flask-app ./helm/flask-app \
     --set replicaCount=3
   ```
7. Commit the chart (with updated `values.yaml`) to `manifests-repo`, push.

## Talking points
- Helm didn't remove the manual step — you still ran a command by hand. It just made *what* you deploy reusable and parameterized (imagine doing this for 5 environments with raw YAML vs. one chart + different `values-*.yaml` files).
