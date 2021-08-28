# Pulumi EKS preview bug

In Pulumi v3.10.1+, `pulumi preview` no longer works if you set an `eks.Cluster`
resource as the parent of another resource. To repro:

```
AWS_DEFAULT_REGION=us-east-1 pulumi preview
```

If you comment out the `parent=cluster` option in the node group, then
`pulumi preview` works fine.
