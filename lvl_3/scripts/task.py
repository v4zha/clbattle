from story import storyTeller 
import sys
if len(sys.argv)>1 and sys.argv[1]=="fast":
    st=storyTeller(3,fast=True)
else:
    st=storyTeller(3)
st.print_story()

