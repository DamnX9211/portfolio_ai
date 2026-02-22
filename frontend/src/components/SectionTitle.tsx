interface Props {
    title: string
}

export default function SectionTitle({ title }: Props) {
    return (
        <h2 className="text-3xl font-semibold mb-6 border-b border-gray-700 pb-2">
            {title}
        </h2>
    )
}