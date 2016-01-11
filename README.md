#run_picardtools_markdups

Examines aligned records in the supplied SAM or BAM file to locate duplicate molecules. All records are then written to the output file with the duplicate records flagged.

```

Development information

date created : Aug 28 2014
last update  : Mar 19  2015
Developer    : Diljot Grewal (dgrewal@bccrc.ca)
Input        : bam file
Output       : bam 
Parameters   : assume_sorted, analysis_type (supports reheader and markduplicates), read_name_regex, opd, mfhfrem, stringency
Seed used    : picardtools/MarkDuplicates.jar

```

###Dependencies

- picardtools
- java


###Known issues



###Last updates

Jan 29 2015: merged run_picardtools and run_picardtools_reheader (developed by Rad Aniba <raniba@bccrc.ca>)

Mar19: separated the reheader and markdups component again.
