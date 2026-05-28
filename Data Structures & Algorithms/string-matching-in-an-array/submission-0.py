from collections import defaultdict

class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.length = 0
        self.words = set()


class SuffixAutomaton:
    def __init__(self):
        self.states = [State()]
        self.last = 0

    def extend(self, ch, word_id):
        cur = len(self.states)
        self.states.append(State())

        self.states[cur].length = self.states[self.last].length + 1
        self.states[cur].words.add(word_id)

        p = self.last

        while p >= 0 and ch not in self.states[p].next:
            self.states[p].next[ch] = cur
            p = self.states[p].link

        if p == -1:
            self.states[cur].link = 0

        else:
            q = self.states[p].next[ch]

            if self.states[p].length + 1 == self.states[q].length:
                self.states[cur].link = q

            else:
                clone = len(self.states)
                self.states.append(State())

                self.states[clone].length = self.states[p].length + 1
                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].link = self.states[q].link

                while p >= 0 and self.states[p].next.get(ch) == q:
                    self.states[p].next[ch] = clone
                    p = self.states[p].link

                self.states[q].link = clone
                self.states[cur].link = clone

        self.last = cur

    def add_word(self, word, word_id):
        self.last = 0

        for ch in word:
            self.extend(ch, word_id)

    def propagate(self):
        order = sorted(
            range(len(self.states)),
            key=lambda i: self.states[i].length,
            reverse=True
        )

        for v in order:
            parent = self.states[v].link

            if parent != -1:
                self.states[parent].words |= self.states[v].words

    def contains_in_other_word(self, word, word_id):
        v = 0

        for ch in word:
            if ch not in self.states[v].next:
                return False

            v = self.states[v].next[ch]

        return len(self.states[v].words - {word_id}) > 0


class Solution:
    def stringMatching(self, words):
        sam = SuffixAutomaton()

        for i, word in enumerate(words):
            sam.add_word(word, i)

        sam.propagate()

        ans = []

        for i, word in enumerate(words):
            if sam.contains_in_other_word(word, i):
                ans.append(word)

        return ans