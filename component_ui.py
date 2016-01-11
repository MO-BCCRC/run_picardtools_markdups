'''
Created on Mar 20, 2014

@author: dgrewal
java -Xmx4G -jar /share/lustre/csiu/apps/picard-tools-1.71/MarkDuplicates.jar 
INPUT=realign/DG1040N_A12968_D0WATACXX_2_hg19.srt.bam 
OUTPUT=realign/DG1040N_A12968_D0WATACXX_2_hg19_dupsFlagged.bam 
METRICS_FILE=realign/DG1040N_A12968_D0WATACXX_2_hg19.paired.metrics.txt 
ASSUME_SORTED=true 
READ_NAME_REGEX="[a-zA-Z0-9]+_[0-9]+:[0-9]+:([0-9]+):([0-9]+):([0-9]+).*" 
OPTICAL_DUPLICATE_PIXEL_DISTANCE=16 
MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=1000 
VALIDATION_STRINGENCY=LENIENT 
TMP_DIR=/share/scratch/csiu_temp/realignment/example/realign
'''

import argparse

chrom_list = map(str, range(1, 23)) + ['X', 'Y']

parser = argparse.ArgumentParser()

parser.add_argument('--input',  
                    required=True, 
                    help='the input bam file')

parser.add_argument('--output',  
                    required=True, 
                    help='the output bam file')

parser.add_argument('--picard_metrics_file', 
                    required = True,
                    help='path to the second fastq file')

parser.add_argument('--assume_sorted',
                    action = 'store_true',
                    help='Assume the input bam is sorted')

parser.add_argument('--read_name_regex',
                    default = "[a-zA-Z0-9]+_[0-9]+:[0-9]+:([0-9]+):([0-9]+):([0-9]+).*" ,
                    help='The regex representing the read names.')

parser.add_argument('--opd', 
                    default = 16,
                    help=' optical duplicate pixel distance')

parser.add_argument('--mfhfrem', 
                    default = 1000,
                    help= ''' max file handles for read ends map ''')

parser.add_argument('--val_stringency', 
                    default = 'LENIENT',
                    help= ''' Validation Stringency ''')

parser.add_argument('--tmp_dir', 
                    required = True,
                    help='path to the temporary dir for intermediate files')

args,unknown = parser.parse_known_args()
