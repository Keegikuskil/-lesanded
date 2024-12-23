tahed = "abcdefghijklmnoprsšzžtuvõäöü"
sonum = "bnüizdvüvvvivüozžzeuziüüišömvbüeuczmmššgübzhnuozhzimzozuozübivcmiüenbüeäümniüazšbievüimovvcgvüuzžindreänzianmrgivcmiüüibnüizivuzvüffmzozzmzvmmvopüdnüun"

for key in range(len(tahed)):
    tehtud = ""
    for ch in sonum:
        if ch in sonum:
            num = tahed.find(ch)
            num = num - key
            if num < 0:
                num = num + len(tahed)
            tehtud = tehtud + tahed[num]
        else:
            translated = translated + ch
    print("Variant %s: %s" % (key, tehtud))
    