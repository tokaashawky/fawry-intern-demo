# Module 5 — GitLab CI: Build & Push Only (14:00 – 14:35)

**Goal:** Automate the Docker build+push step (Module 2) with a GitLab pipeline. Deploy stays manual (`helm upgrade` by hand)

## Steps for students

1. In `app-repo`, add the first version of `.gitlab-ci.yml` (build + push stages only):
   ```yaml
   stages:
     - build
     - push

   variables:
     IMAGE_TAG: "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"

   build:
     stage: build
     script:
       - docker build -t $IMAGE_TAG ./app

   push:
     stage: push
     script:
       - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin $CI_REGISTRY
       - docker build -t $IMAGE_TAG ./app
       - docker push $IMAGE_TAG
   ```
2. Set CI/CD variables in GitLab (Settings → CI/CD → Variables): `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` (or rely on GitLab's built-in registry defaults).
3. Commit and push — watch the pipeline run in the GitLab UI: **build → push**.
4. Confirm the new image tag (`$CI_COMMIT_SHORT_SHA`) appears in the registry.
5. Now deploy it **manually**, exactly like Module 4, but referencing the new tag:
   ```bash
   helm upgrade flask-app ./helm/flask-app \
     --set image.tag=<the-short-sha-from-the-pipeline> 
   ```
6. Refresh the browser — new version live, but notice: *you* still had to run the `helm upgrade` yourself, using a tag you had to go find in the GitLab UI.

## Talking points
- Ask: "What's still manual here?" → getting the image tag, and running the deploy command. That's exactly what Module 6 removes.
- This half-automated state is intentionally awkward — most real teams pass through exactly this stage before adding a deploy job.

