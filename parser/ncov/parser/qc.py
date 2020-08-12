'''
A parser for the qc metrics file generated by the COG-UK Nextflow pipeline.  The
generated file contains a header line and a data line with pre-defined columns.
'''

import re
import glob


def write_qc_summary(summary):
    '''
    A function to write the QC data line to output in the order:
        * sample
        * num_consensus_snvs
        * num_consensus_n
        * num_consensus_iupac
        * num_variants_snv
        * num_variants_indel
        * num_variants_indel_triplet
        * mean_sequencing_depth
        * median_sequencing_depth
        * qpcr_ct
        * collection_date
        * num_weeks
        * genome_completeness
        * qc_pass

    Arguments:
        * summary: a dictionary containing the sample QC details

    Return Value:
        None
    '''
    summary_line = '\t'.join([
        summary['sample'],
        str(summary['num_consensus_snvs']),
        str(summary['num_consensus_n']),
        str(summary['num_consensus_iupac']),
        str(summary['num_variants_snvs']),
        str(summary['num_variants_indel']),
        str(summary['num_variants_indel_triplet']),
        str(summary['mean_sequencing_depth']),
        str(summary['median_sequencing_depth']),
        str(summary['qpcr_ct']),
        str(summary['collection_date']),
        str(summary['num_weeks']),
        str(summary['genome_completeness']),
        str(summary['qc_pass'])])
    print(summary_line)


def write_qc_summary_header(header=['sample',
                                    'num_consensus_snvs',
                                    'num_consensus_n',
                                    'num_consensus_iupac',
                                    'num_variants_snv',
                                    'num_variants_indel',
                                    'num_variants_indel_triplet',
                                    'mean_sequencing_depth',
                                    'median_sequencing_depth',
                                    'qpcr_ct',
                                    'collection_date',
                                    'num_weeks',
                                    'genome_completeness',
                                    'qc_pass']):
    '''
    Write the header for the QC summary data

    Arguments:
        * header: a list containing the column headers

    Return Value:
        None
    '''
    print('\t'.join(header))


def collect_qc_summary_data(path, pattern='.summary.qc.tsv'):
    '''
    An aggregation function to collect individual sample based QC summary data
    and create a single file with all samples.

    Arguments:
        * path:     full path to the <sample>.summary.qc.tsv files
        * pattern:  file pattern for the sample files (default: .summary.qc.tsv)

    Return Value:
        data: a list containing the summary line data
    '''
    files = glob.glob(path + "/*" + pattern)
    data = []
    for file in files:
        with open(file) as file_p:
            for line in file_p:
                # skip the header
                if re.match("^sample\tnum_consensus_snvs\tnum_consensus_n", line):
                    continue
                data.append(line.rstrip())
    return data
