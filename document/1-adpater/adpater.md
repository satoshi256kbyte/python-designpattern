```mermaid
classDiagram
    Student
    class Student{
        year: int
        department: string
        cource: string        
        num : int
        string code()
    }
```

```mermaid
classDiagram
    Student --> ReiwaStudent : extends
    ReiwaStudent <|-- SeirekiInterface : implements
    ReiwaStudent
    class Student{
        year: int
        department: string
        cource: string               
        num : int
        string code()
    }
    class ReiwaStudent{
        string seireki_cd()
    }
    class SeirekiInterface {
        <<Interface>>
        string seireki_cd()
    }
```