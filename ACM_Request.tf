resource "aws_acm_certificate" "cert" {
  domain_name       = "helloworld.com"
  validation_method = "DNS"

  tags = {
    Environment = "production"
  }
}

resource "aws_acm_certificate_validation" "cert_validation" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [aws_route53_record.cert_validation.fqdn]
}
