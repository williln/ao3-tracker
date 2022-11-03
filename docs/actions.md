# GitHub Actions 

## `new_tbr.yml`

### Purpose: Adding new items to your TBR. 

**When It Happens** 

- When an issue is opened or reopened 
- When an issue is labeled 
- When an issue is edited  

**Requires the issue have been opened using the `add-to-tbr.md` template.** 

**What Happens: Technical Explanation**

- Checks it for the label `tbr`. If it is not labeled "tbr," then stops the workflow. 
- If it is labeled "tbr," then the body of the issue is parsed into JSON and the result printed to the console. 
- The link is saved in the output of the action step and passed to a Python script. 
- If the label is present, comments on the issue. 
- Once the issue has been commented, this closes the issue and adds the label `tbr-done`

**Upshot** 

When you submit an "Add to TBR" issue, an action will run that will take the link in the issue and do nothing with it. But it knows it's there. 
