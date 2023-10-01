# CNN Classifer Project

### Workflow

1. research/trials
2. config.yaml, params.yaml
3. entity
4. components
5. pipeline
6. training
7. prediction
8. test your package
9. dvc for reproducing the pipeline

## Sample Code for Streamlit
```
import streamlit as st

st.header("welcome to streamlit")

if st.button("click me"):
    st.write("button clicked")
    
option=st.checkbox("check this box")

if option:
    st.write("checkbox is checked")

```