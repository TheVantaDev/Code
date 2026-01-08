
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        List <String> l=new ArrayList<>();
        List<String> elec = new ArrayList<>();
        List<String> groc = new ArrayList<>();
        List<String> pharm = new ArrayList<>();
        List<String> rest = new ArrayList<>();
        boolean v[]=new boolean[code.length];
        for(int i=0;i<code.length;i++)
        { int count=0;
            if (code[i] == null) {
                v[i] = false;
                continue;
            }
            for (int j = 0; j < code[i].length(); j++) {
                   char ch = code[i].charAt(j);
     if ((ch >= 65 && ch <= 90)   
    || (ch >= 97 && ch <= 122) 
    || (ch >= 48 && ch <= 57)  
    || (ch == 95))
    { count++;
    }
}
 if (code[i].length() > 0 && count == code[i].length()) {
                v[i] = true;
            }}
for(int i=0;i<code.length;i++)
{
    if(v[i]!=isActive[i]) v[i]=false;
}
for(int i=0;i<businessLine.length;i++)
{
     if(businessLine[i].equals("electronics") && v[i]) elec.add(code[i]);

    else if(businessLine[i].equals("grocery") && v[i]) groc.add(code[i]);
    else if(businessLine[i].equals("pharmacy") && v[i]) pharm.add(code[i]);
    else if(businessLine[i].equals("restaurant") && v[i]) rest.add(code[i]);
}
Collections.sort(elec);
Collections.sort(groc);
Collections.sort(pharm);
Collections.sort(rest);
l.addAll(elec);
l.addAll(groc);
l.addAll(pharm);
l.addAll(rest);

        return l;
    }
}