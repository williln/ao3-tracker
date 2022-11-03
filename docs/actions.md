# GitHub Actions 

## `new_tbr.yml`

**Purpose**: Adding new items to your TBR. 

When a new issue is created in this repo, this action: 

- Checks it for the label `tbr`
- If the label is present, comments on the issue. 
- Once the issue has been commented, this closes the issue and adds the label `tbr-done`
