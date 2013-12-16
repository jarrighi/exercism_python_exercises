class DNA:
  def __init__(self, strand):
    self.dna_strand = strand

  def to_rna(self):
    rna_strand = ''

    for bp in self.dna_strand:
      if bp == 'T':
        rna_strand += 'U'

      elif bp in 'GCA':
        rna_strand += bp

      else:
        print "Transacription Failed: Invalid Polymer"
        return None

    return rna_strand