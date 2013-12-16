class DNA:
  def __init__(self, strand):
    self.dna_strand = strand
    self.rna_bp_for_dna_bp = {'G': 'G', 'C':'C', 'A': 'A', 'T': 'U'}

  def to_rna(self):
    rna_strand = ''

    for bp in self.dna_strand:
      try: 
        rna_strand += self.rna_bp_for_dna_bp[bp]

      except KeyError:
        print "Invalid Polymer"

    return rna_strand