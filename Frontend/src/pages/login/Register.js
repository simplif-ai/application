import React from 'react';

const Register = ({ login }) => (
  <form onSubmit={login}>
    <label placeholder="First Name" type="" htmlFor="email" />
    <input type="email" name="email" required />
    <label placeholder="email" type="" htmlFor="email" />
    <input type="email" name="email" required />
    <label placeholder="password" type="" htmlFor="password" />
    <input type="password" name="password" required />
    <input type="submit" value="Submit" />
    <a href='/login'>Already have an account? Sign In</a>
  </form>
);

export default Register;