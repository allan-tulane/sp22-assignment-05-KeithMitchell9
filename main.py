test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
  if (S == "") and (T != ""):
    return(len(T))
  elif (T == "") and (S != ""):
    return(len(S))
  elif (S == "") and (T == ""):
    return 0
  else:
    if (S[0] == T[0]):
      return(MED(S[1:], T[1:]))
    else:
      return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  key = S,T
  if not T:
    MED[len(S), 0] = len(S)
    return MED[len(S), 0]
  elif not S:
    MED[0, len(T)] = len(T)
    return MED[0, len(T)]
  elif key is in MED:
    return MED[key]
  elif (S[0] == T[0]):
    return(fast_MED(S[1:], T[1:]))
  else:
    MED[key] = (1 + min(fast_MED(S, T[1:]), fast_MED(S[1:], T), fast_MED(S[1:], T[1:])))
    return MED[key]

def fast_align_MED(S, T, MED={}):
  key = S,T
  if (S, T) in MED:
    return MED[(S, T)]
  elif not S and not T:
    return 0
  elif not S:
    MED[0, len(T)] = len(T)
    return MED[0, len(T)] *'-', T
  elif not T:
    MED[len(S),0] = len(S)
    return S,MED[len(S),0] * '-'
  elif key is in MED:
    return MED[key]
  elif S[0] == T[0]:
    return fast_MED(S[1:], T[1:])
  else:
    first = 1 + fast_MED(S, T[1:])
    second = 1 + fast_MED(S[1:], T)
    third = 1 + fast_MED(S[1:], T[1:])
    minimum = min(first, second, third)
    MED[(S, T)] = minimum
    return MED[(S, T)]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
