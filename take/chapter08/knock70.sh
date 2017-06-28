awk '{print "+1", $0}' rt-polarity.pos > sentiment.txt
awk '{print "-1", $0}' rt-polarity.neg >> sentiment.txt
