import {useParams} from "react-router-dom";
import React, {useEffect, useState} from "react";
import axios from "axios";


export const EventDetail = () => {
    const params = useParams();

    const [data, setData] = useState();

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/event/' + params.id)
            .then(resp => {
                setData(resp.data[0]);
            })
    }, []);

    const [name, setName] = useState();
    const [phone, setPhone] = useState();
    const [email, setEmail] = useState();

    const [memberId, setMemberId] = useState();

    const onSubmit = () => {
        axios.post("http://localhost:8000/member/", {fio: name, phone: phone, email: email})
            .then(resp => {
                setMemberId(resp.data)
            })

        axios.post("http://localhost:8000/member_in_event/", {event_id: params.id, member_id: memberId['member_id']})
            .then(resp => console.log(resp))
    }

    if (data) {
        return (
            <div className="App">
                <h2 className="title">{data.name}</h2>
                <img className="detail_image" src={data.file} alt=""/>
                <p className="detail_image">{data.description}</p>
                <p className="detail_image"><b>Дата проведения:</b> {data.dat}</p>
                <p className="detail_image"><b>Тип мероприятия:</b> {data.event_type.name}</p>
                <h3>Зарегистрируйтесь на мероприятие!</h3>
                <div className="form">
                    <p className="text-field">
                        <label className="text-field__label" htmlFor="">ФИО</label>
                        <input className="text-field__input" type="text" onChange={(e) => setName(e.target.value)}
                               value={name}/>
                    </p>
                    <p className="text-field">
                        <label className="text-field__label" htmlFor="">Телефон</label>
                        <input className="text-field__input" type="text" onChange={(e) => setPhone(e.target.value)}
                               value={phone}/>
                    </p>
                    <p className="text-field">
                        <label className="text-field__label" htmlFor="">Email</label>
                        <input className="text-field__input" type="text" onChange={(e) => setEmail(e.target.value)}
                               value={email}/>
                    </p>

                    <button className="btn" onClick={onSubmit}><span>Зарегистрироваться</span></button>
                </div>
            </div>
        )
    }

}