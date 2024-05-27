import React, {useEffect, useState} from "react";
import axios from "axios";
import AnimationOnScroll from 'react-animate-on-scroll';


export const EventList = () => {
    const [data, setData] = useState();

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/event/')
            .then(resp => {

                setData(resp.data)
            })
    }, []);


    return (
        <div className="App">
            <div className="banner">
                <img className="banner_image" src="/all-friend_x2.webp"/>
                <p className="banner_text">Добро пожаловать в мир незабываемых событий с нашим сервисом по организации
                    мероприятий! Мы — команда профессионалов, готовых превратить ваши идеи в реальность и создать
                    атмосферу, о которой будут вспоминать долгие годы. Независимо от того, нужно ли вам провести
                    корпоративное мероприятие, свадьбу, день рождения или любое другое событие, мы возьмем на себя всю
                    организационную работу, чтобы вы могли насладиться каждым моментом без лишних хлопот. Доверьте нам
                    свои мечты, и мы превратим их в яркую реальность!</p>
            </div>

            <h2 className="title">Наши мероприятия</h2>
            {data?.map(el => {
                return (
                    <AnimationOnScroll animateIn="animate__bounceIn" className="event_item">
                        <img className="event_item_image" src={el.file} alt=""/>
                        <h3><a href={el.id}>{el.name}</a></h3>
                    </AnimationOnScroll>
                )
            })}
        </div>
    );
}