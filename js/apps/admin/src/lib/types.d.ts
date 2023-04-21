export interface IUser{
    id: number,
    name: string,
    date: string,
    status: string,
    formula: string,
    kyc: string,
    linked_accounts: number
}

export interface IAdmin{
    id: number,
    name: string,
    email: string,
    role: string
}