# | ::::::: Fancy progressbar for lengthy operations
# |
if [[ ${#OPTION[@]} -gt 5 ]]; then
  # Note: We use eval here because we want the functions to be available in this script
  if [[ "$(uname)" = "Darwin" ]]; then
    eval "$(curl -so- ${PROGRESS_URL})" 2> /dev/null
  else
    eval "$(wget -qO- ${PROGRESS_URL})"  2> /dev/null
  fi
fi



PROGRESS_URL="https://raw.githubusercontent.com/phenonymous/shell-progressbar/1.0/progress.sh"
