import { useEffect, useState } from "react";
import { Search } from "../../components/Search";
import { Popular } from "./layout/Popular";
import { New } from "./layout/New";
import { Recommend } from "./layout/Recommend";

export const MainPage = ({ mode }) => {

  const [popularQuote,setPopularQuote]= useState({});
  const [newQuote, setNewQuote] = useState([]);
  const [recomQuote, setRecomQuote]=useState([]);

    /** dummy data */
    useEffect(()=>{
        const p = {'id':0,'title':'title','creater':'author book','subData':'pub3030',
            'content':'content contentcontentcontentcontentcontent',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        }
        setPopularQuote(p);

        const n = [{'id':1,'title':'title','creater':'author book1','subData':'pub3030',
            'content':'content ffffffffffffffff',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        },
      {'id':2,'title':'title','creater':'author book2','subData':'slkdc',
            'content':'content skddkkdddkll',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        },
      {'id':3,'title':'title','creater':'author book3','subData':'sdfkdslk',
            'content':'content newnqwlmkcwmclwmelmclmdkfnsdjclsdaklmlc',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        }]
        setNewQuote(n);

        const r = [{'id':4,'title':'title','creater':'author book1','subData':'pub3030',
            'content':'content recommend contentrecommend contentrecommend contentrecommend content',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        },
      {'id':5,'title':'title','creater':'author book2','subData':'slkdc',
            'content':'content recommend contentkkrecommend contentkmfskdm',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        },
      {'id':6,'title':'title','creater':'author book3','subData':'sdfkdslk',
            'content':'content merry christmas harry',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        }]
        setRecomQuote(r);
    },[])

  return (
    <>
      <div className="flex justify-center">
        <Search/>
      </div>
      <div className="mt-12">
        {mode}     
        {/* popular */}
        <Popular popularQuote={popularQuote} />

        {/* new */}
        <New newQuote={newQuote} />

        {/* recommend */}
        <Recommend recomQuote={recomQuote}/>

      </div>
    </>
  );
};
