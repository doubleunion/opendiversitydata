OpenDiversityData.org JSON Schema
=================

This directory contains a [JSON Schema](http://json-schema.org/ 'JSON Schema Homepage') for the U.S. government's [EEO-1 Survey](http://www.eeoc.gov/employers/eeo1survey/ 'EEO-1 Survey Homepage').

Unfortunately, JSON Schema syntax does not allow comments. Some explanation of choices made in the schema are contained instead within this document.

At the highest level, there are two required properties of the JSON object composing the data for a single EEO-1 report: the `meta` property and the `section_d` property. Other than the `meta` property, every other property - i.e., those beginning with `section_` describes a section of an EEO-1 report, as represented in the [sample EEO-1 form](http://www.eeoc.gov/employers/eeo1survey/upload/eeo1-2.pdf 'Sample EEO-1 Reporting Form') linked in [the instructions for EEO-1 reporting](http://www.eeoc.gov/employers/eeo1survey/2007instructions.cfm 'Instructions for EEO-1 Reporting') and as represented in the PDFs that many companies release as the public version of their EEO-1 report, as for example [Dell's](http://money.cnn.com/technology/storysupplement/diversity-data/dell-2010-EEO-1.html 'Dell's 2010 EEO-1 Report') (here embedded in the webpage as an image, which is unfortunately quite common).

Sections A, B, and C of the standard EEO-1 report are not required in the schema because they don't contain the data of interest, and it's possible that some presentations of publicly released EEO-1 data won't include them.

The `section_d` property of the report object contains the data of interest. It describes an array of exactly ten objects because there are ten job categories across which companies must report diversity statistics. The categories themselves are enumerated as possible values of the `job_category` property of each array object. The `data` for each object in the array is itself an array, where each array item is an object containing three fields: `race`, which is a string value, limited to the seven categories defined for the EEO-1 Survey); `men` and `women` as integer values with an minimum of zero. The array value of `data` must contain seven items, since there are seven possible categories of `race`.

### Caveats

In its present form, the schema requires ten objects because there are ten job categories in an EEO-1 report and seven objects within each job category's data array because there are seven races for reporting under EEO-1. In both of these data arrays, each object must be unique within the array, but it would still be possible to submit ill-formed data if a job category label is repeated (but one of the other ten is missing) but the data for the (duplicate) category is different. A much more verbose schema would be required to guard against this case, so we are opting to take on the risk of such ill-formed data (at least for now).
