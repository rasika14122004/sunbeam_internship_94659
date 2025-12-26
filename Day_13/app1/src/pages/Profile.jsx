import React, { useEffect, useState } from 'react'
import Navbar from '../components/Navbar'
import { getUserProfile, updateProfile } from '../services/userService'
import { toast } from 'react-toastify'

function Profile() {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [mobile, setMobile] = useState('')

    useEffect(() => {
        console.log('Profile component loaded')
        getProfile()
    }, [])

    const getProfile = async () => {
        const token = sessionStorage.getItem('token')
        const result = await getUserProfile(token)
        if (result.status == "success") {
            const user = result.data[0]
            setName(user.name)
            setEmail(user.email)
            setMobile(user.mobile)
        }
    }

    const update = async () => {
        const token = sessionStorage.getItem('token')
        const result = await updateProfile(token, mobile)
        if (result.status == "success")
            toast.success("Profile Updated")
    }
    return (
        <div>
            <Navbar />
            <div className='container'>
                <div className='mt-3 mb-3'>
                    <input type="text" class="form-control" id="inputEmail" value={email} />
                </div>
                <div className='mb-3 d-flex'>
                    <input type="text" className="form-control me-3" id="inputName" value={name} />
                    <input type="tel" className="form-control ms-3" id="inputMobile" value={mobile} onChange={e => setMobile(e.target.value)} />
                </div>
                <div>
                    <button className="btn btn-success" onClick={update}>Update</button>
                </div>
            </div>
        </div>
    )
}

export default Profile
