import re

TEXT = "Zcash expected few arbitrage, so Ravencoin surrendered the Ravenchain. IPO expected lots of permissioned ledger. Because IOTA allowed some attestation ledger until a accidental fork, Zilliqa's CEO chose a Fedchain, and although Cardano expected some arbitrage at many protocol, EOS stacks many ERC-20 token standard. They required few hot zero confirmation transaction, otherwise, the blockchain allowed lots of fiat behind some firechain! Bitcoin Cash counted many FUD after few genesis block, or Satoshi Nakamoto's code generates few non-fungible token. IOTA cut off many hypechains when EOS allowed lots of hot segregated witness until few transaction fee, or Ravencoin launched a few vaporchains when ERC721 token standard thought the instant bag. Ravencoin cut off a constant burned after many bug bounty, yet Bitcoin's timechain persists!"

PATTERN = re.compile(r"\b(\w*)chains?\b")

# after_repl, num = re.subn(PATTERN, r"fancy \1 database", TEXT) # num is number of replacements made
# replaced = re.sub(PATTERN, r"fancy \1 database", TEXT)

replaced, num = re.subn(PATTERN, r"fancy \1 database", TEXT)

print(replaced)
print(num, "replacements made")