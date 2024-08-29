## Meetup : Deploy Serverless Infrastructure 

### Check Setup

`curl -sL https://git.io/_has | bash -s terraform aws git zip unzip python3`

- Join the Slack Community: https://bit.ly/devinfra-slack
- Shared Repo: https://github.com/appcd-demo/devinfra-aug-2024
- AWS Access: https://bit.ly/devinfra-aws
- appcd: https://cloud.appcd.io/


### Setup

- Connect to WiFi
- Install aws cli -> https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Install terraform -> https://developer.hashicorp.com/terraform/install?product_intent=terraform
- Make sure python3 is installed
- Make sure git is also installed
- [Optional] macos: `brew install appcd-dev/homebrew-appcd/appcd`

---
## Workshop: hello-kitty
### on appcd

- set filename to app.zip
- enable function url
- environment variable: IMAGES_BUCKET=<your-bucket-name>>

### clone the lambda source repo
- clone hello-kitty, cd hello-kitty
- `make build` and copy build/app.zip to exported IaC folder

### deploy exported IaC

- copy above zip file in the directory where we exported
- run `terraform apply`
- cd hello-kitty
- copy images to the s3 bucket
  - `aws s3 cp images/ s3://<your-bucket-name>/ --recursive`

- `terraform output`
  - aws cli `aws lambda get-function-url-config --function-name <your-function-name> | jq '.FunctionUrl'

- Cleanup: `terraform destroy`
