# GitHub Actions 

## `new_tbr.yml`

### Purpose: Adding new items to your TBR

### When 

- When an issue is opened or reopened 
- When an issue is labeled 
- When an issue is edited  

**Requires the issue have been opened using the `add-to-tbr.md` template.**

### What 

- Checks it for the label `tbr`. If it is not labeled "tbr," then stops the workflow. 
- If it is labeled "tbr," then the body of the issue is parsed into JSON and the result printed to the console. 
- The link is saved in the output of the action step and saved in a file called `generated.txt`. The idea is to have an action that picks up on changes made to `main` and then reads that file, processes the link, and deletes the file so it's ready to be re-created for the next one. 
- Comments on the issue to indicate that processing is done
- Once the issue has been commented, this closes the issue and adds the label `tbr-done`

### All you need to know

When you submit an "Add to TBR" issue, an action will run that will take the link in the issue and do nothing with it. But it knows it's there. 
