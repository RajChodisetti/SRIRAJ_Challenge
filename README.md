Heres my approach

I would use following AWS services to host thi sstatic website
- Amazon S3: Store static HTML, CSS, JavaScript, and image files. S3 is highly durable and available, and it integrates well with other AWS services.
- Amazon CloudFront: Use as a Content Delivery Network (CDN) to cache and deliver the static content closer to the users, which decreases latency and increases the speed of content delivery.
- AWS Certificate Manager (ACM): Provides a way to manage SSL/TLS certificates for your domain, including renewal and deployment, at no additional cost.
- Amazon Route 53: Manage DNS and connect domain names with your CloudFront distributions.
- AWS WAF (Web Application Firewall): Protect the application from common web exploits and bots that might affect availability, compromise security, or consume excessive resources.
- AWS Lambda@Edge: (optional) To run server-side code closer to the user which can help with tasks like URL rewrites, security headers, or other edge computations without managing servers.
- IAM Policies: Restrict access to the S3 buckets and other resources using fine-grained IAM policies
- Logging and Monitoring: Use AWS CloudTrail and Amazon CloudWatch to log and monitor all access and requests to the resources.
I will make this website secure by following
- HTTPS: Use ACM for handling SSL/TLS certificates which are then used with CloudFront to serve content over HTTPS.
- Security Headers: Implement security headers using Lambda@Edge to add headers like Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, etc.
For configuring AWS services, i will use Terraform.

s3_bucket_config.tf : 
Configures an S3 bucket to store and serve static website content, setting up public read access and defining index and error documents 

CloudFront_Setup.tf :
Creates a CloudFront distribution to deliver content globally with low latency, configures HTTPS using an SSL certificate from ACM, and enforces HTTPS traffic.

ACM_Request.tf :
Requests an SSL/TLS certificate from AWS Certificate Manager for your domain, facilitating secure communication over HTTPS.

Route53_config.tf :
Manages DNS settings using Route 53, including configuration for DNS validation of the ACM certificate and setting up domain records.
Sets up a Route 53 health check for the website, monitoring its availability via HTTPS and integrating with DNS settings for smart traffic routing based on health status.

Now, 
For serving static content, a web server isn't necessary because S3, along with CloudFront, can serve static content directly. However, if a server-side component is needed, you can still set up an EC2 instance using Terraform and configure it

For Security , The Terraform scripts above handle HTTPS redirection and SSL/TLS setup using ACM and CloudFront. AWS WAF can be added for enhanced security.

For Testing , We also included Health Check in Route53 to monitor the health directly. We can also use tools like Terratest that allows us to write automated tests.



