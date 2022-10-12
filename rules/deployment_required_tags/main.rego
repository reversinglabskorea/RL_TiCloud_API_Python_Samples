package rules

required_deployment_labels {
  input.metadata.labels["app.kubernetes.io/name"]
  input.metadata.labels["app.kubernetes.io/instance"]
  input.metadata.labels["app.kubernetes.io/version"]
  input.metadata.labels["app.kubernetes.io/component"]
  input.metadata.labels["app.kubernetes.io/part-of"]
  input.metadata.labels["app.kubernetes.io/managed-by"]
}

deny[msg] {
  input.kind = "Deployment"  
  not required_deployment_labels
	msg := {
		# Mandatory fields
		"publicId": "deployment_required_tags",
		"title": "Require Kubernetes recommended labels",
		"severity": "high",
		"msg": "input.metadata.labels", # must be the JSON path to the resource field that triggered the deny rule
		# Optional fields
		"issue": "",
		"impact": "Internal tools won't work correctly as missing key information",
		"remediation": "Add common labels under the app.kubernetes.io namespace",
		"references": ["https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/"],
	}
}
