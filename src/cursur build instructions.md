# Build Instructions for creating formatted docuemnts using the ai first principles.md content

## Objective

## Step 1 - properly parse content
pull content from "ai first principles.md"

Create name-value pairs for content to be used later in file creation. The name value pairs should follow this pattern:
| Name           | Instruction to pull the value    |
| -------------- | -------------------------------- |
| Title        | The title will be the only text marked by the Heading Level 1 tag |
| Description  | The text between the title and the next heading |
| value-title-1 through value-title-n | value titles are marked with the heading level 3 markdown tag under the "## Vales" headin |
| value-desc-1 through value-desc-n   | value descriptions is the text below the value title NOT INCLUDING TEXT MARKED BETWEEN **not this**|
| value-act-1 through value-act-n     | value actions IS the text below the value title MARKED BETWEEN **this** |
| value-ret-1 through value-rat-n     | value rationale is the footnote associated with the value |
| tenet-title-1 through tenet-title-n | tenet titles are marked with the heading level 3 markdown tag under the "## Vales" headin |
| tenet-desc-1 through tenet-desc-n   | tenet descriptions is the text below the value title NOT INCLUDING TEXT MARKED BETWEEN **not this**|
| tenet-act-1 through tenet-act-n     | tenet actions IS the text below the value title MARKED BETWEEN **this** |
| tenet-rat-1 through tenet-rat-n     | tenet rationale is the footnote associated with the value |

## Quality Assurance Checklist
Before executing any build step:
- [ ] Read the exact file path from instructions
- [ ] Verify the directory structure exists or needs to be created  
- [ ] Confirm the exact filename to be created
- [ ] Execute file creation in the specified location
- [ ] Verify the file was created in the correct location

**IMPORTANT**: Follow instructions - if it says "/build directory", use exactly "/build directory", not any other variation.

## Step 2 - build a simple html file
you will be creating a new html file based on a template and saving the new file in the 
/build directory
open the "ai first principles template.html" file

Find and replace the placeholders for the values you have pulled in Step 1
-- NOTE: YOU MAY NEED TO CREATE PLACEHOLDERS IF YOU HAVE MORE VALUES OR TENETS THAN THERE IS IN THE TEMPALTE

placeholders will look like this : "{{placeholder name}}"

important: when dealing with the tenet-rat-n and value-rat-n content, they have new lines . You need to preserve new lines by adding paragraph tags to text s that the content is appropriatly spaced 

Save this new document as "ai first principles.html" in the /build directory (if this file already exists, replace it)

## Step 3 - Craft AI First Principles for Prompts content
you will be creating a new json file based on a template and saving the new file in the 
/build directory
open the "ai first principles prompt template.jsonl" file

Find and replace the placeholders for the values you have pulled in Step 1
-- NOTE: YOU MAY NEED TO CREATE PLACEHOLDERS IF YOU HAVE MORE VALUES OR TENETS THAN THERE IS IN THE TEMPALTE

placeholders will look like this : "{{placeholder name}}"

important: when dealing with the tenet-rat-n and value-rat-n content, they have new lines . You need to preserve new lines by adding paragraph tags to text s that the content is appropriatly spaced 

Save this new document as "ai first principles prompt.json" in the /build directory (if this file already exists, replace it)


## Step 4 - build jupyter notebook
instructions to come later - skip this step
