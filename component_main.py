'''

Created on May 12, 2014

@author: dgrewal

component for titan pipeline
filter positions from input file that aren't in dbsnp file.
'''
from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    def __init__(self,component_name='run_picardtools', component_parent_dir=None, seed_dir=None):
        self.version = '1.0.0'
        ## initialize ComponentAbstract 
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)
        
    def make_cmd(self,chunk=None):
        #if the markdups flag is not set, skip the step, just create a copy 
        #of input file and continue
        if not self.args.run_component:
            cmd = 'cp '+ self.args.input +' ' +self.args.output
            cmd_args = []
            return cmd, cmd_args

        cmd = self.requirements['java'] +' -Xmx4G -jar ' +\
              self.requirements['picardtools_markdups']
          
        cmd_args = ['INPUT='+self.args.input,
                    'OUTPUT='+self.args.output,
                    'METRICS_FILE='+self.args.picard_metrics_file,
                    'READ_NAME_REGEX="'+self.args.read_name_regex+'"',
                    'OPTICAL_DUPLICATE_PIXEL_DISTANCE='+str(self.args.opd),
                    'MAX_FILE_HANDLES_FOR_READ_ENDS_MAP='+str(self.args.mfhfrem),
                    'VALIDATION_STRINGENCY='+self.args.val_stringency,
                    'TMP_DIR='+self.args.tmp_dir
                    ]

        if self.args.assume_sorted:
            cmd_args.append('ASSUME_SORTED=TRUE')
        else:
            cmd_args.append('ASSUME_SORTED=FALSE')
       
        return cmd, cmd_args

    def test(self):
        import component_test
        component_test.run()
                    
def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()
    comp.test()
    
    
if __name__ == '__main__':
    import component_ui
    _main()
