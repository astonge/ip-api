export GCLOUD_PROJECT="jpgr-wtf" 
export REPO="ip-api"
export REGION="us-west1"
export IMAGE="ipapi-image"
export IMAGE_TAG=${REGION}-docker.pkg.dev/$GCLOUD_PROJECT/$REPO/$IMAGE
# Build the image:
docker build -t $IMAGE_TAG -f Dockerfile --platform linux/x86_64 .
# Push it to Artifact Registry:
docker push $IMAGE_TAG
