export default function SignUp() {
    return (
        <div>
            <h1>Create account</h1>

            <form>
                <center>
                    <table>
                        <tr>
                            <td><label>First Name</label></td>
                            <td><input type="text" name="first_name"/></td>
                        </tr>

                        <tr>
                            <td><label>Last Name</label></td>
                            <td><input type="text" name="last_name" /></td>
                        </tr>
                        
                        <tr>
                            <td><label>Email</label></td>
                            <td><input type="email" name="email" placeholder="wsuid@wichita.edu" /></td>
                        </tr>

                        <tr>
                            <td><label>Date of Birth</label></td>
                            <td><input type="date" name="dob" /></td>
                        </tr>

                        <tr>
                            <td><label>Zipcode</label></td>
                            <td><input type="text" name="zipcode" placeholder="676767" /></td>
                        </tr>

                        <tr>
                            <td><label>Password</label></td>
                            <td><input type="password" name="password"/></td>
                        </tr>

                        <tr>
                            <td><label>Confirm Password</label></td>
                            <td><input type="password" name="confirmPassword"/></td>
                        </tr>

                        <tr>
                            <td></td>
                            <td><button type="submit">Create Account</button></td>
                        </tr>
                    </table>
                </center>
            </form>

            <p>already have a account? <a href="/login">sign in</a></p>

        </div>
    )
}