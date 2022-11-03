# GitHub Actions 

## `new_tbr.yml`

**Purpose**: Adding new items to your TBR. 

When a new issue is created in this repo, this action: 

- Gets the body of the issue comment and saves it in a variable 
- Checks it for the label `tbr`
- If the label is present, comments on the issue. 
