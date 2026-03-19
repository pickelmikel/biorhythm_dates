import streamlit as st

perfect_compat_finder = st.Page('perfect_compatibility_finder.py',
    title='Perfect Compatibility Finder')
biorhythm_checker = st.Page('biorhythm_checker.py',
    title='Biorhythm Checker')
pg = st.navigation(
    pages=[perfect_compat_finder, biorhythm_checker],
    position='top',
    expanded=True)
pg.run()
