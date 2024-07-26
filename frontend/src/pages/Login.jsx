import React from 'react';
import Form from "../components/Form";

function Login() {
//   console.log("Login component rendering");
  return (
    <div>
      <h1>Login Page</h1>
      <Form route="/api/token/" method="login" />
    </div>
  );
}

export default Login;