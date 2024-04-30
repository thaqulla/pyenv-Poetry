import { useState } from 'react'
import axios, { AxiosResponse } from "axios";
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  // データの型を定義（例：string、number、オブジェクト型など）
  interface DataType {
    name: string;
    age: number;
    // 他に必要なプロパティがあれば追加する
  }


  const [count, setCount] = useState(0);
  const [data, setData] = useState<DataType | null>(null);
  const url = "http://127.0.0.1:8000";
  const GetData = () => {
		axios.get(url).then((res:AxiosResponse) => {
			setData(res.data);
		});
	};

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank" rel="noopener noreferrer">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <div>
			<div>ここに処理を書いていきます</div>
			{data ? <div>{data.name}({data.age} years_old)</div> : <button onClick={GetData}>データを取得</button>}
		</div>
    </>
  )
}

export default App
