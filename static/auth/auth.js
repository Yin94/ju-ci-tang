document.forms[0].onsubmit = async e => {
  e.preventDefault();
  try {
    const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]')
      .value;
    const usr_name = document.querySelector("input[name='username']").value;
    const pswd = document.querySelector("input[name='password']").value;
    const result = await fetch('/apis/auth/signin/', {
      method: 'POST',
      mode: 'cors',
      headers: { 'X-CSRFToken': csrf },
      body: JSON.stringify({ usr_name, pswd })
    });
    const json = await result.json();
    if (json.errors) throw json.errors[0];
    else {
      localStorage.setItem('token', json['token']);
      window.location.href = '/';
    }
  } catch (err) {
    //error logic
    console.log(err.message);
  }
};

document.querySelector('.btn-danger').addEventListener('click', e => {
  e.target.parentElement.parentElement.reset();
});
