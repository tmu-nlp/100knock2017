try:
    from xml.etree.ElementTree import *
    tree = parse("nlp.txt.xml")
    elem = tree.getroot()
    for w in elem.findall(".//word"):
        print(w.text) # solution for 53
except FileNotFoundError:
    import corenlp
    import xmltodict
    #from subprocess import call
    # corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2016-10-31"
    corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2014-08-27"
    raw_text_directory = "sample_raw_text"
    # command = corenlp.init_corenlp_command(corenlp_path=corenlp_dir, memory="3g",  properties='default.properties') + ' -filelist + "./nlp.txt" -outputDirectory +"./"'
    # call(command,shell=True)
    parsed = corenlp.batch_parse(raw_text_directory, corenlp_dir, raw_output=True)
    parsed_list = []
    while True:
        parsed_list.append(parsed.__next__())
    parsed_xml = xmltodict.unparse(dict(parsed_list))
    print(parsed_xml)
